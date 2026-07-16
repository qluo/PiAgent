from agent.agent import Agent


class FakeLlm:
    def __init__(self):
        self.prompts = []

    def answer(self, user_text):
        self.prompts.append(user_text)
        return f"answer to {user_text}"


def test_agent_respond_returns_llm_answer():
    llm = FakeLlm()
    agent = Agent(
        face_state=None,
        wake_word=None,
        stt=None,
        tts=None,
        llm=llm,
        tools={},
    )
    agent.agents_md = ""

    assert agent.respond("hello") == "answer to hello"


def test_agent_respond_includes_agents_md_in_llm_prompt():
    agent = Agent(
        face_state=None,
        wake_word=None,
        stt=None,
        tts=None,
        llm=FakeLlm(),
        tools={},
    )
    agent.agents_md = "Answer in one sentence."

    assert agent.respond("hello") == (
        "answer to Agent instructions:\n"
        "Answer in one sentence.\n\n"
        "User request:\n"
        "hello"
    )
