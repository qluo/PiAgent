from agent.agent import Agent


class Tool:
    pass


def test_agent_stores_the_tools_it_is_given():
    face_state = Tool()
    wake_word = Tool()
    stt = Tool()
    tts = Tool()
    llm = Tool()
    search = Tool()

    agent = Agent(
        face_state=face_state,
        wake_word=wake_word,
        stt=stt,
        tts=tts,
        llm=llm,
        tools={"search": search},
    )

    assert agent.face_state is face_state
    assert agent.wake_word is wake_word
    assert agent.stt is stt
    assert agent.tts is tts
    assert agent.llm is llm
    assert agent.tools["search"] is search
