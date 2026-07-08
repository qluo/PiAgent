class Agent:
    def __init__(self, face_state, wake_word, stt, tts, llm, tools):
        self.face_state = face_state
        self.wake_word = wake_word
        self.stt = stt
        self.tts = tts
        self.llm = llm
        self.tools = tools

    def run(self):
        """Main agentic loop."""
        # Lesson 4: Implement The Main Agent Loop
        #
        # Goal:
        # Move the loop idea from demo.py into this clean Agent class.
        #
        # Concept to learn:
        # The Agent is the orchestrator. It decides the order of actions,
        # but each tool does its own special job.
        #
        # Small first step:
        # Copy the high-level shape from demo.py:
        # 1. Set face to "idle".
        # 2. Wait for wake word: self.wake_word.wait().
        # 3. Set face to "listening".
        # 4. Get user text: self.stt.listen_and_transcribe().
        # 5. Set face to "thinking".
        # 6. Get response: self.respond(user_text).
        # 7. Set face to "speaking".
        # 8. Speak response: self.tts.speak(response).
        #
        # Test idea:
        # Use fake tools first. If the loop works with fake tools, then swap
        # in one real tool at a time.
        pass

    def respond(self, user_text: str) -> str:
        """Produce a response, optionally using tools."""
        # Lesson 4, then Lessons 7 and 8:
        #
        # Goal:
        # Decide whether the agent should answer directly with the LLM or use
        # a tool first.
        #
        # Small first step:
        # Return self.llm.answer(user_text).
        #
        # Later:
        # If the user says "search" or "look up", call:
        #   self.tools["search"].search(user_text)
        # Then pass the search result into:
        #   self.llm.answer_with_context(user_text, context)
        #
        # Expected return value:
        # A string that can be sent to self.tts.speak(...).
        return ""
