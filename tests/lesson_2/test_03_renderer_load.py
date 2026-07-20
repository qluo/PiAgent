from PIL import Image

from face import states
from face.renderer import FaceRenderer


def test_renderer_loads_frames_before_draw_is_implemented():
    renderer = FaceRenderer()

    loaded_frames = renderer.load()
    frames = getattr(renderer, "frames", loaded_frames)

    assert isinstance(frames, dict)
    assert states.IDLE in frames
    assert frames[states.IDLE], "The idle state should have at least one frame."


def test_renderer_load_uses_folder_names_and_resets_frame_indexes(tmp_path, monkeypatch):
    idle_dir = tmp_path / "idle"
    idle_dir.mkdir()
    Image.new("RGBA", (1, 1), "red").save(idle_dir / "02.png")
    Image.new("RGBA", (1, 1), "blue").save(idle_dir / "01.png")

    renderer = FaceRenderer(faces_dir=str(tmp_path))
    monkeypatch.setattr(renderer, "_setup_display", lambda: None)

    frames = renderer.load()

    assert list(frames) == ["idle"]
    assert len(frames["idle"]) == 2
    assert renderer.frame_indexes == {"idle": 0}
