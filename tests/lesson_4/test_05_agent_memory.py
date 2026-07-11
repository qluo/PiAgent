from agent.agent import Agent
from agent.tools.memory import MemoryTool


class RecordingLlm:
    def __init__(self):
        self.requests = []

    def answer(self, prompt):
        self.requests.append(prompt)
        return "A helpful answer"


def test_remember_command_saves_fact_without_calling_llm(tmp_path):
    llm = RecordingLlm()
    memory = MemoryTool(tmp_path)
    agent = Agent(None, None, None, None, llm, {}, memory=memory)
    agent.agents_md = "Be helpful."

    response = agent.respond("Remember that my favorite color is blue")

    assert response == "I will remember that my favorite color is blue."
    assert memory.facts() == ["my favorite color is blue"]
    assert llm.requests == []
    assert "Remember that my favorite color is blue" in memory.recent_conversation()


def test_agent_uses_memory_in_order_and_records_answer(tmp_path):
    llm = RecordingLlm()
    memory = MemoryTool(tmp_path)
    memory.remember("my name is Sam")
    memory.record_turn("Hi", "Hello Sam")
    agent = Agent(None, None, None, None, llm, {}, memory=memory)
    agent.agents_md = "Be concise."

    assert agent.respond("What is my name?") == "A helpful answer"

    prompt = llm.requests[0]
    assert prompt.index("Agent instructions:") < prompt.index("Remembered user data")
    assert prompt.index("Remembered user data") < prompt.index("Recent conversation")
    assert prompt.index("Recent conversation") < prompt.index("User request:")
    assert "A helpful answer" in memory.recent_conversation()
