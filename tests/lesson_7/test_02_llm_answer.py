from agent.tools.llm import LlmTool


def test_llm_answer_returns_text_after_implementation():
    tool = LlmTool()

    answer = tool.answer("Say hello in five words or less.")

    assert isinstance(answer, str)
    assert answer.strip()
