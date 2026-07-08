from agent.tools.stt import SpeechToTextTool


def test_stt_tool_has_listen_and_transcribe_method():
    tool = SpeechToTextTool()

    assert hasattr(tool, "listen_and_transcribe")
