import pytest

from agent.tools.wake_word import WakeWordTool


def test_wait_uses_the_keyboard_helper_in_keyboard_mode(monkeypatch):
    tool = WakeWordTool(mode="keyboard")
    calls = []

    monkeypatch.setattr(tool, "_wait_for_keyboard_wake", lambda: calls.append("keyboard"))
    monkeypatch.setattr(tool, "_wait_for_microphone_wake", lambda: calls.append("microphone"))

    tool.wait()

    assert calls == ["keyboard"]


def test_wait_rejects_an_unknown_mode():
    with pytest.raises(ValueError, match='"microphone" or "keyboard"'):
        WakeWordTool(mode="button").wait()
