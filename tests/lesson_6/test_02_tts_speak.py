from agent.tools.tts import TextToSpeechTool


def test_tts_speak_finishes_without_error():
    tool = TextToSpeechTool()

    assert tool.speak("Hello from my Pi agent") is None
