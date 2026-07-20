import requests

from agent.tools.llm import LlmTool


class FakeResponse:
    def raise_for_status(self):
        return None

    def json(self):
        return {"response": "  Hello from Ollama.  "}


def test_llm_answer_posts_the_prompt_and_returns_only_answer_text(monkeypatch):
    calls = []

    def fake_post(url, **kwargs):
        calls.append((url, kwargs))
        return FakeResponse()

    monkeypatch.setattr(requests, "post", fake_post)
    tool = LlmTool(
        model_name="lesson-model",
        base_url="http://ollama.test:11434/",
        timeout=12.5,
    )

    answer = tool.answer("Say hello in five words or less.")

    assert answer == "Hello from Ollama."
    assert calls == [
        (
            "http://ollama.test:11434/api/generate",
            {
                "json": {
                    "model": "lesson-model",
                    "prompt": "Say hello in five words or less.",
                    "stream": False,
                },
                "timeout": 12.5,
            },
        )
    ]
