import pytest

from face import states
from face.renderer import FaceRenderer


def test_renderer_draws_one_state_after_load():
    renderer = FaceRenderer()
    renderer.load()

    result = renderer.draw(states.IDLE)

    assert result is None
    assert (
        getattr(renderer, "last_drawn_state", None) == states.IDLE
        or getattr(renderer, "current_state", None) == states.IDLE
    )


def test_renderer_advances_and_wraps_each_states_frame_index():
    renderer = FaceRenderer()
    renderer.frames = {states.IDLE: [object(), object()]}
    renderer.frame_indexes = {states.IDLE: 0}

    renderer.draw(states.IDLE)
    renderer.draw(states.IDLE)

    assert renderer.frame_indexes[states.IDLE] == 0
    assert renderer.last_drawn_state == states.IDLE


def test_renderer_rejects_a_state_without_frames():
    renderer = FaceRenderer()
    renderer.frames = {states.IDLE: [object()]}

    with pytest.raises(ValueError, match="No face frames loaded"):
        renderer.draw(states.THINKING)
