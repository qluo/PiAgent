from agent.tools.stt import SpeechToTextTool


def test_keyboard_stt_returns_typed_text(monkeypatch):
    tool = SpeechToTextTool()

    monkeypatch.setattr("builtins.input", lambda _prompt="": "hello agent")

    result = tool.listen_and_transcribe()

    assert result == "hello agent"
