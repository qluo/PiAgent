from agent.tools.stt import SpeechToTextTool


def test_keyboard_stt_returns_typed_text(monkeypatch):
    tool = SpeechToTextTool(mode="keyboard")

    monkeypatch.setattr("builtins.input", lambda _prompt="": "hello agent")

    result = tool.listen_and_transcribe()

    assert result == "hello agent"


def test_microphone_stt_saves_transcribes_and_removes_temp_audio(tmp_path, monkeypatch):
    tool = SpeechToTextTool(mode="microphone")
    wav_path = tmp_path / "question.wav"
    wav_path.write_bytes(b"audio")
    calls = []

    monkeypatch.setattr(tool, "listen_until_silence", lambda: calls.append("listen") or b"audio")
    monkeypatch.setattr(tool, "save_temp_wav", lambda audio: calls.append(("save", audio)) or wav_path)
    monkeypatch.setattr(tool, "run_whisper", lambda path: calls.append(("whisper", path)) or "hello")

    assert tool.listen_and_transcribe() == "hello"
    assert calls == ["listen", ("save", b"audio"), ("whisper", wav_path)]
    assert not wav_path.exists()
