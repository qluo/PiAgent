import demo


def test_fake_llm_has_starter_responses():
    llm = demo.FakeLlmTool()

    assert "Pi Agent" in llm.answer("what is your name?")
    assert "Hello" in llm.answer("hello")
    assert "computer" in llm.answer("tell me a joke")
