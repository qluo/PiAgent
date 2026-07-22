"""AGENTS.md checkpoint for Lesson 9.

This terminal-only demo shows the prompt built from the project's persistent
instructions and one user request:

    uv run python -m demos.lesson9_agent_instructions_demo
"""

from __future__ import annotations

import argparse

from agent.agent import Agent


class RecordingLlm:
    """Fake LLM that keeps the prompt it receives for display."""

    def __init__(self) -> None:
        self.prompt = ""

    def answer(self, prompt: str) -> str:
        self.prompt = prompt
        return "The prompt includes the project instructions and your request."


def parse_args() -> argparse.Namespace:
    """Read one user request to combine with AGENTS.md."""
    parser = argparse.ArgumentParser(description="Show Pie Agent's persistent instructions in a prompt.")
    parser.add_argument("question", nargs="?", default="What can you help me with?")
    return parser.parse_args()


def main() -> None:
    """Build and display a prompt without requiring Ollama or hardware."""
    args = parse_args()
    llm = RecordingLlm()
    agent = Agent(
        face_state=None,
        wake_word=None,
        stt=None,
        tts=None,
        llm=llm,
        tools={},
    )

    print(f"You: {args.question}")
    print(f"Loaded AGENTS.md: {'yes' if agent.agents_md else 'no'}")
    print(f"Agent: {agent.respond(args.question)}")
    print("\nPrompt sent to the LLM:\n")
    print(llm.prompt)


if __name__ == "__main__":
    main()
