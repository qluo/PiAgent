class FaceController:
    def __init__(self, face_state, renderer=None):
        self.face_state = face_state
        self.renderer = renderer

    def run(self):
        """Continuously render the face matching the latest FaceState."""
        # Lesson 2: Face Controller
        #
        # Goal:
        # Keep the face display updated while the agent is doing other work.
        #
        # Concept to learn:
        # This method runs in a background thread. It should loop forever:
        # read the current state, draw that state's next frame, pause briefly,
        # and repeat.
        #
        # Suggested package:
        # - time.sleep: pause between frames.
        #
        # Small first step:
        # Print the current state whenever it changes.
        #
        # Real version idea:
        # 1. Call self.renderer.load() once before the loop.
        # 2. Inside the loop, read state = self.face_state.get().
        # 3. Call self.renderer.draw(state).
        # 4. Sleep for a short time, such as 0.1 seconds.
        #
        # Expected return value:
        # Nothing. This method keeps running.
        pass
