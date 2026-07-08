from face import states
from face.renderer import FaceRenderer


def test_renderer_loads_frames_before_draw_is_implemented():
    renderer = FaceRenderer()

    loaded_frames = renderer.load()
    frames = getattr(renderer, "frames", loaded_frames)

    assert isinstance(frames, dict)
    assert states.IDLE in frames
    assert frames[states.IDLE], "The idle state should have at least one frame."
