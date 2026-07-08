from agent.tools.llm import LlmTool


def test_llm_tool_stores_local_ollama_settings():
    tool = LlmTool()

    assert tool.model_name
    assert tool.base_url.startswith("http://localhost")
