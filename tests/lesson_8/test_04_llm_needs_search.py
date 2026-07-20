from agent.tools.llm import LlmTool


def test_needs_search_uses_the_llm_decision(monkeypatch):
    tool = LlmTool()
    prompts = []

    monkeypatch.setattr(
        tool, "answer", lambda prompt: prompts.append(prompt) or "SEARCH"
    )
    assert tool.needs_search("What is the weather today?") is True
    assert "What is the weather today?" in prompts[0]
    assert "SEARCH or NO_SEARCH" in prompts[0]

    monkeypatch.setattr(tool, "answer", lambda _prompt: "NO_SEARCH")
    assert tool.needs_search("What is two plus two?") is False
