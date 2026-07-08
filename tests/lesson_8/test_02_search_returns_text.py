from agent.tools.search import SearchTool


def test_search_returns_text_after_implementation():
    tool = SearchTool()

    result = tool.search("Raspberry Pi")

    assert isinstance(result, str)
    assert result.strip()
