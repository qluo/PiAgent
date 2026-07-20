import agent.tools.search as search_module
from agent.tools.search import SearchTool


def test_search_tool_has_search_method():
    tool = SearchTool()

    assert hasattr(tool, "search")


class FakeDdgs:
    results = []
    error = None
    calls = []

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def text(self, query, **kwargs):
        self.__class__.calls.append((query, kwargs))
        if self.error:
            raise self.error
        return self.results


def test_search_formats_the_first_result_and_uses_configured_settings(monkeypatch):
    FakeDdgs.calls = []
    FakeDdgs.error = None
    FakeDdgs.results = [
        {"title": "Lesson title", "body": "A useful snippet", "href": "https://example.test"},
        {"title": "Ignored", "body": "Ignored", "href": "https://ignored.test"},
    ]
    monkeypatch.setattr(search_module, "DDGS", FakeDdgs)

    result = SearchTool(max_results=2, region="wt-wt").search("Pie Agent news")

    assert result == "Title: Lesson title\nSummary: A useful snippet\nURL: https://example.test"
    assert FakeDdgs.calls == [
        ("Pie Agent news", {"region": "wt-wt", "max_results": 2})
    ]


def test_search_returns_helpful_messages_for_empty_results_and_errors(monkeypatch):
    monkeypatch.setattr(search_module, "DDGS", FakeDdgs)
    FakeDdgs.calls = []
    FakeDdgs.error = None
    FakeDdgs.results = []

    assert SearchTool().search("nothing") == "No search results found for nothing."

    FakeDdgs.error = RuntimeError("network unavailable")
    assert "Search failed for nothing: network unavailable" == SearchTool().search("nothing")
