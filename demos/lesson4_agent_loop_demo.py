"""Fake-tool checkpoint for Lesson 4.

This runs the student's clean Agent class without microphone, speaker, or
Ollama setup. It makes the order of face-state and tool calls visible:

    uv run python -m demos.lesson4_agent_loop_demo
"""

from __future__ import annotations

from agent.agent import Agent
from face import states
from face.state import FaceState


class ConsoleFaceState(FaceState):
    """FaceState that prints each state change for this terminal-only demo."""

    def set(self, state: str) -> None:
        super().set(state)
        print(f"Face: {state}")


class KeyboardWakeWordTool:
    """Stand in for the wake-word tool until Lesson 3 is connected."""

    def wait(self) -> None:
        input("\nPress Enter to wake the agent...")


class KeyboardSpeechToTextTool:
    """Stand in for speech-to-text until Lesson 5 is connected."""

    def listen_and_transcribe(self) -> str:
        return input("You: ")


class EchoLlmTool:
    """Stand in for the local LLM until Lesson 7 is connected."""

    def answer(self, user_text: str) -> str:
        return f"You said: {user_text}"


class PrintTextToSpeechTool:
    """Stand in for a speaker until Lesson 6 is connected."""

    def speak(self, text: str) -> None:
        print(f"Agent: {text}")


def main() -> None:
    """Run the student's Agent loop with terminal-only tools."""
    face_state = ConsoleFaceState()
    agent = Agent(
        face_state=face_state,
        wake_word=KeyboardWakeWordTool(),
        stt=KeyboardSpeechToTextTool(),
        tts=PrintTextToSpeechTool(),
        llm=EchoLlmTool(),
        tools={},
    )

    print("Lesson 4 agent-loop demo. Press Ctrl+C to stop.")
    try:
        agent.run()
    except KeyboardInterrupt:
        face_state.set(states.IDLE)
        print("\nStopped.")


if __name__ == "__main__":
    main()
