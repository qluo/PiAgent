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
