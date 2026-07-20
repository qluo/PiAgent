import agent.tools.wake_word as wake_word_module
from agent.tools.wake_word import WakeWordTool


class AudioColumn:
    def copy(self):
        return "audio chunk"


class AudioData:
    def __getitem__(self, key):
        assert key == (slice(None), 0)
        return AudioColumn()


class FakeInputStream:
    def __init__(self, *, callback, **kwargs):
        self.callback = callback
        self.kwargs = kwargs

    def __enter__(self):
        self.callback(AudioData(), 0, None, None)
        return self

    def __exit__(self, *_args):
        return False


class FakeModel:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def predict(self, audio_chunk):
        assert audio_chunk == "audio chunk"
        return {"wake": 0.6}


def test_microphone_wake_word_returns_when_model_reaches_threshold(monkeypatch):
    monkeypatch.setattr(
        wake_word_module,
        "sd",
        type("SoundDevice", (), {"InputStream": FakeInputStream}),
    )
    monkeypatch.setattr(wake_word_module, "Model", FakeModel)

    tool = WakeWordTool(model_path="lesson-model", threshold=0.6)

    assert tool.wait() is None
