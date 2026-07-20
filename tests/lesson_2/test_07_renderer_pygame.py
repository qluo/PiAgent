from PIL import Image

from face.renderer import FaceRenderer


class FakeScreen:
    def __init__(self):
        self.fills = []
        self.blits = []

    def get_size(self):
        return (20, 10)

    def fill(self, color):
        self.fills.append(color)

    def blit(self, surface, position):
        self.blits.append((surface, position))


class FakePygame:
    QUIT = "quit"

    def __init__(self):
        self.event = type("Event", (), {"get": staticmethod(lambda: [])})
        self.image = type(
            "Image", (), {"fromstring": staticmethod(lambda data, size, mode: (data, size, mode))}
        )
        self.display = type("Display", (), {"flip": self._flip})
        self.flips = 0

    def _flip(self):
        self.flips += 1


def test_renderer_draws_a_loaded_frame_with_pygame():
    renderer = FaceRenderer()
    screen = FakeScreen()
    pygame = FakePygame()
    renderer._screen = screen
    renderer._pygame = pygame

    renderer._draw_with_pygame(Image.new("RGBA", (2, 2), "red"))

    assert screen.fills == [(0, 0, 0)]
    assert len(screen.blits) == 1
    assert pygame.flips == 1
