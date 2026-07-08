from face import states
from face.controller import FaceController
from face.state import FaceState


class RecordingRenderer:
    def __init__(self):
        self.drawn_states = []

    def draw(self, state):
        self.drawn_states.append(state)


def test_controller_run_once_draws_current_face_state():
    face_state = FaceState()
    face_state.set(states.THINKING)
    renderer = RecordingRenderer()
    controller = FaceController(face_state, renderer=renderer)

    controller.run_once()

    assert renderer.drawn_states == [states.THINKING]
