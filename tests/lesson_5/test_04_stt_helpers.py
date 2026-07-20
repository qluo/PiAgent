import subprocess
import sys
import wave
from pathlib import Path
from types import ModuleType

from agent.tools.stt import SpeechToTextTool


def test_save_temp_wav_uses_mono_16_bit_audio():
    tool = SpeechToTextTool(sample_rate=8_000)

    wav_path = tool.save_temp_wav(b"\x00\x00\x01\x00")
    try:
        with wave.open(str(wav_path), "rb") as wav_file:
            assert wav_file.getnchannels() == 1
            assert wav_file.getsampwidth() == 2
            assert wav_file.getframerate() == 8_000
            assert wav_file.readframes(2) == b"\x00\x00\x01\x00"
    finally:
        wav_path.unlink(missing_ok=True)


def test_run_whisper_uses_configured_command_and_cleans_timestamp_output(monkeypatch):
    tool = SpeechToTextTool(model_path="model.bin", whisper_binary="whisper")
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, "[00:00] hello\n[00:01] world\n", "")

    monkeypatch.setattr(subprocess, "run", fake_run)

    assert tool.run_whisper(Path("question.wav")) == "hello world"
    assert calls == [
        (["whisper", "-m", "model.bin", "-f", "question.wav", "-nt"],
         {"check": True, "capture_output": True, "text": True})
    ]


class FakeRawInputStream:
    chunks = [b"\x00\x00", b"\xe8\x03", b"\x00\x00"]

    def __init__(self, *, callback, **kwargs):
        self.callback = callback
        self.kwargs = kwargs

    def __enter__(self):
        for chunk in self.chunks:
            self.callback(chunk, 0, None, None)
        return self

    def __exit__(self, *_args):
        return False


def test_listen_until_silence_keeps_speech_and_following_quiet_audio(monkeypatch):
    sounddevice = ModuleType("sounddevice")
    sounddevice.RawInputStream = FakeRawInputStream
    monkeypatch.setitem(sys.modules, "sounddevice", sounddevice)
    tool = SpeechToTextTool(seconds=1, silence_seconds=0.1, silence_threshold=500)

    assert tool.listen_until_silence() == b"\xe8\x03\x00\x00"
