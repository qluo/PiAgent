from agent.tools.stt import SpeechToTextTool


def test_loudness_measures_16_bit_audio_volume():
    tool = SpeechToTextTool()

    quiet_audio = (0).to_bytes(2, "little", signed=True) * 4
    loud_audio = (1_000).to_bytes(2, "little", signed=True) * 4

    assert tool.loudness(quiet_audio) == 0
    assert tool.loudness(loud_audio) == 1_000


def test_loudness_handles_empty_and_negative_samples():
    tool = SpeechToTextTool()
    negative_audio = (-500).to_bytes(2, "little", signed=True) * 2

    assert tool.loudness(b"") == 0
    assert tool.loudness(negative_audio) == 500
