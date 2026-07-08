class SearchTool:
    """Web search tool using DuckDuckGo search.

    This follows the original Raspberry Pi agent repo's simple approach:
    use the `duckduckgo_search` package and its `DDGS` helper.

    Setup idea:
    - Install project packages: uv pip install -r requirements.txt
    - Import DDGS: from duckduckgo_search import DDGS
    """

    def search(self, query: str) -> str:
        """Search for information and return text context."""
        # Lesson 8: Tools - Web Search
        #
        # Goal:
        # Search the web and return a short piece of text that the LLM can use.
        #
        # Suggested package:
        # - duckduckgo-search: provides the DDGS helper.
        #
        # Import after installing requirements:
        #   from duckduckgo_search import DDGS
        #
        # Concept to learn:
        # Search tools usually return lots of data. Your job is to shape that
        # data into a small, useful context string.
        #
        # Small first step:
        # Ask for one result with max_results=1.
        #
        # Real version idea:
        # 1. Open DDGS with: with DDGS() as ddgs:
        # 2. Call ddgs.text(query, region="us-en", max_results=1).
        # 3. Pull out the title, href, and body/snippet.
        # 4. Return a short string for the LLM.
        #
        # Expected return value:
        # A short string like:
        #   "Title: ...\nSummary: ...\nURL: ..."
        return ""
