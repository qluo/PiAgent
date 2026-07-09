class FaceRenderer:
    def __init__(self, faces_dir: str = "faces") -> None:
        """Create the face renderer.

        Inputs:
        - faces_dir: folder that contains one subfolder per face state.

        Output:
        - None. Starts with no loaded frames.
        """
        self.faces_dir = faces_dir
        self.frames: dict[str, list[object]] = {}
        self.frame_indexes: dict[str, int] = {}
        self.last_drawn_state: str | None = None

    def load(self) -> dict[str, list[object]]:
        """Load face assets from disk.

        Inputs:
        - None. Reads image files from self.faces_dir.

        Output:
        - A dictionary mapping each face state to a list of loaded frames.
          Example: {"idle": [frame1, frame2]}.

        Side effects:
        - Stores the same dictionary on self.frames.
        """
        # Lesson 2: Face Renderer
        #
        # Goal:
        # Load the Mini panda bot PNG files from the faces/ folders.
        #
        # Suggested packages:
        # - pathlib: find image files in folders.
        # - Pillow: load PNG files if you render with Pillow/Tkinter.
        # - pygame: load PNG files if you render with pygame.
        #
        # Concept to learn:
        # Each folder name is a face state. Each PNG inside that folder is one
        # animation frame for that state.
        #
        # Small first step:
        # Build a dictionary like:
        #   self.frames["thinking"] = [image1, image2, image3]
        #
        # Expected result:
        # After load() runs, draw("thinking") can find thinking frames.
        return self.frames

    def draw(self, state: str) -> None:
        """Draw the next frame for a face state.

        Inputs:
        - state: face state name, such as "idle", "thinking", or "speaking".

        Output:
        - None. The result appears on the display.

        Side effects:
        - Draws one frame.
        - Usually updates self.last_drawn_state and a frame index.
        """
        # Lesson 2: Face Renderer
        #
        # Goal:
        # Show the next PNG frame for the requested state.
        #
        # Suggested package:
        # - pygame: good for fullscreen display on Raspberry Pi.
        #
        # Concept to learn:
        # Animation is just showing images in order:
        # frame 1, frame 2, frame 3, then back to frame 1.
        #
        # Small first step:
        # Draw the first image for the state without animation.
        #
        # Real version idea:
        # 1. Look up the frame list for state.
        # 2. Keep a frame index for each state.
        # 3. Draw the current frame.
        # 4. Move the frame index forward.
        # 5. Store self.last_drawn_state = state so your test can check it.
        #
        # Expected return value:
        # Nothing. The result appears on the display.
        pass
