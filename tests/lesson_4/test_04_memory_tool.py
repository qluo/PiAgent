from agent.tools.memory import MemoryTool


def test_memory_tool_creates_readable_markdown_files(tmp_path):
    memory = MemoryTool(tmp_path)

    assert (tmp_path / "conversation.md").read_text() == "# Conversation Memory\n\n"
    assert (tmp_path / "facts.md").read_text() == "# Remembered Facts\n\n"


def test_memory_tool_persists_facts_and_recent_turns(tmp_path):
    memory = MemoryTool(tmp_path, max_turns=2)
    memory.remember("my name is Sam")
    memory.record_turn("one", "first")
    memory.record_turn("two", "second")
    memory.record_turn("three", "third")

    restored_memory = MemoryTool(tmp_path, max_turns=2)

    assert restored_memory.facts() == ["my name is Sam"]
    conversation = restored_memory.recent_conversation()
    assert "one" not in conversation
    assert "two" in conversation
    assert "three" in conversation
