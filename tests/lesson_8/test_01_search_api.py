from agent.tools.search import SearchTool


def test_search_tool_has_search_method():
    tool = SearchTool()

    assert hasattr(tool, "search")
