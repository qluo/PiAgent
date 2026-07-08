from unittest.mock import patch

import demo


def test_demo_agent_can_quit():
    face_state = demo.FaceState()
    agent = demo.Agent(
        face_state=face_state,
        wake_word=demo.FakeWakeWordTool(),
        stt=demo.FakeSpeechToTextTool(),
        llm=demo.FakeLlmTool(),
        tts=demo.FakeTextToSpeechTool(),
    )

    with patch("builtins.input", side_effect=["", "quit"]):
        agent.run()

    assert face_state.get() == "idle"
