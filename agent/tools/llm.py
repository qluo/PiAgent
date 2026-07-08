class LlmTool:
    """Local LLM tool powered by Ollama.

    Teaching goal:
    - Run the model on the Raspberry Pi instead of using a cloud API.
    - Start with a small open model so students can see the full loop work.

    Setup idea:
    - Install Ollama on the Raspberry Pi.
    - Pull a small model, for example: ollama pull llama3.2:1b
    - Ollama usually runs locally at: http://localhost:11434
    """

    def __init__(self, model_name: str = "llama3.2:1b"):
        self.model_name = model_name
        self.base_url = "http://localhost:11434"

    def answer(self, user_text: str) -> str:
        """Answer directly using a local Ollama model."""
        # Lesson 7: Local LLM
        #
        # Goal:
        # Send the user's text to a local Ollama model and return its answer.
        #
        # Suggested package:
        # - requests: makes HTTP calls to Ollama's local API.
        #
        # Concept to learn:
        # Ollama runs a local web server at self.base_url. Your Python code
        # sends a prompt to that server and receives generated text back.
        #
        # Small first step:
        # Test Ollama in the terminal first:
        #   ollama run llama3.2:1b
        #
        # Real version idea:
        # 1. Send a POST request to an Ollama endpoint.
        # 2. Include self.model_name and user_text in the request body.
        # 3. Parse the JSON response.
        # 4. Return only the answer text.
        #
        # Expected return value:
        # A string response from the local model.
        return ""

    def answer_with_context(self, user_text: str, context: str) -> str:
        """Answer using tool context and a local Ollama model."""
        # Lesson 8: Search + LLM
        #
        # Goal:
        # Give the local LLM extra information from a tool, such as web
        # search results, before it answers.
        #
        # Concept to learn:
        # The LLM does not automatically know what your search tool found.
        # You must include the search result inside the prompt.
        #
        # Small first step:
        # Build one combined prompt string:
        #   "User question: ... Search result: ..."
        #
        # Real version idea:
        # 1. Combine user_text and context into a clear prompt.
        # 2. Send that prompt to Ollama the same way answer(...) does.
        # 3. Return only the final answer text.
        #
        # Expected return value:
        # A string response that uses the tool context.
        return ""
