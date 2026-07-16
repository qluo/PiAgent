"""Local Ollama checkpoint for Lesson 7.

Start Ollama and pull the teaching model first:

    ollama pull gemma3:1b
    uv run python -m demos.lesson7_llm_demo
"""

from __future__ import annotations

import argparse

from agent.tools.llm import LlmTool


def parse_args() -> argparse.Namespace:
    """Read the local model name and question."""
    parser = argparse.ArgumentParser(description="Ask Pi Agent's local Ollama model.")
    parser.add_argument("question", nargs="?", default="What is a Raspberry Pi?")
    parser.add_argument("--model", default="gemma3:1b")
    return parser.parse_args()


def main() -> None:
    """Ask one question and print the local model's response."""
    args = parse_args()
    llm = LlmTool(model_name=args.model)
    print(f"Model: {args.model}")
    print(f"You: {args.question}")
    print(f"Agent: {llm.answer(args.question)}")


if __name__ == "__main__":
    main()
