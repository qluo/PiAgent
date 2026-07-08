from pathlib import Path

from face import states


def test_face_assets_exist_for_each_state():
    expected_states = [
        states.IDLE,
        states.LISTENING,
        states.THINKING,
        states.SPEAKING,
        states.ERROR,
        states.CAPTURING,
        states.WARMUP,
    ]

    for state in expected_states:
        folder = Path("faces") / state
        pngs = sorted(folder.glob("*.png"))
        assert pngs, f"Missing PNG frames in {folder}"
