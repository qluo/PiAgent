from agent.tools.llm import LlmTool


def test_llm_tool_accepts_a_remote_ollama_url():
    tool = LlmTool(base_url="http://192.168.1.50:11434/")

    assert tool.base_url == "http://192.168.1.50:11434"


def test_llm_tool_uses_environment_url(monkeypatch):
    monkeypatch.setenv("PI_AGENT_OLLAMA_URL", "https://ollama.home.example")

    tool = LlmTool()

    assert tool.base_url == "https://ollama.home.example"
