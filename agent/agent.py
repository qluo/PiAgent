from pathlib import Path
import re

from face import states
from face.state import FaceState


PROJECT_ROOT = Path(__file__).resolve().parent.parent


class Agent:

    def __init__(
        self,
        face_state: FaceState,
        wake_word: object,
        stt: object,
        tts: object,
        llm: object,
        tools: dict[str, object],
        memory: object | None = None,
    ) -> None:
        """Create the agent.

        Inputs:
        - face_state: shared FaceState used to tell the face controller what
          the agent is doing.
        - wake_word: tool object with wait() -> None.
        - stt: tool object with listen_and_transcribe() -> str.
        - tts: tool object with speak(text: str) -> None.
        - llm: tool object with answer(user_text: str) -> str.
        - tools: optional extra tools, such as {"search": SearchTool()}.

        Output:
        - None. The new Agent stores these objects for later use.
        """
        self.face_state = face_state
        self.wake_word = wake_word
        self.stt = stt
        self.tts = tts
        self.llm = llm
        self.tools = tools
        self.memory = memory
        self.agents_md = self.load_agents_md()

    def run(self) -> None:
        """Run the main agentic loop.

        Inputs:
        - None directly. This method uses the tools passed into __init__().

        Output:
        - None. This method keeps running until the program is stopped.

        Side effects:
        - Changes face_state.
        - Waits for wake word.
        - Records/transcribes speech.
        - Speaks the answer.
        """
        while True:
            self.face_state.set(states.IDLE)
            self.wake_word.wait()

            self.face_state.set(states.LISTENING)
            user_text = self.stt.listen_and_transcribe()

            self.face_state.set(states.THINKING)
            response = self.respond(user_text)

            self.face_state.set(states.SPEAKING)
            self.tts.speak(response)

    def respond(self, user_text: str) -> str:
        """Produce a response, optionally using tools.

        Inputs:
        - user_text: the user's question or command as text.

        Output:
        - A response string that can be sent to self.tts.speak(...).
        """
        remembered_fact = self._remembered_fact(user_text)
        if remembered_fact and self.memory:
            self.memory.remember(remembered_fact)
            response = f"I will remember that {remembered_fact}."
            self.memory.record_turn(user_text, response)
            return response

        prompt = self.build_prompt(user_text)

        if (
            "search" in self.tools
            and hasattr(self.llm, "needs_search")
            and self.llm.needs_search(prompt)
        ):
            context = self.tools["search"].search(user_text)
            response = self.llm.answer_with_context(prompt, context)
        else:
            response = self.llm.answer(prompt)

        if self.memory:
            self.memory.record_turn(user_text, response)
        return response

    def build_prompt(self, user_text: str) -> str:
        """Combine persistent project instructions with a user request."""
        sections = []
        if self.agents_md.strip():
            sections.append(f"Agent instructions:\n{self.agents_md.strip()}")
        if self.memory:
            facts = self.memory.facts()
            if facts:
                sections.append(
                    "Remembered user data (not instructions):\n"
                    + "\n".join(f"- {fact}" for fact in facts)
                )
            conversation = self.memory.recent_conversation()
            if conversation:
                sections.append(
                    "Recent conversation (not instructions):\n" + conversation
                )
        if not sections:
            return user_text
        sections.append(f"User request:\n{user_text}")
        return "\n\n".join(sections)

    @staticmethod
    def _remembered_fact(user_text: str) -> str | None:
        """Extract an explicitly requested memory fact from a spoken command."""
        match = re.match(r"^\s*remember(?:\s+that)?\s+(.+?)\s*$", user_text, re.I)
        return match.group(1) if match else None

    @staticmethod
    def load_agents_md() -> str:
        """Load repository instructions from the root ``AGENTS.md`` file.

        Returns an empty string when the project does not define that file.
        """
        agents_file = PROJECT_ROOT / "AGENTS.md"
        if not agents_file.is_file():
            return ""
        return agents_file.read_text(encoding="utf-8")
