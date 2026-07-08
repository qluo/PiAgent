from face import states
from face.state import FaceState


def test_face_state_starts_idle():
    face_state = FaceState()

    assert face_state.get() == states.IDLE


def test_face_state_set_and_get():
    face_state = FaceState()

    face_state.set(states.LISTENING)

    assert face_state.get() == states.LISTENING
