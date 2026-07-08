from agent.tools.wake_word import WakeWordTool


def test_wake_word_tool_has_wait_method():
    tool = WakeWordTool()

    assert hasattr(tool, "wait")
