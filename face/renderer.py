class FaceRenderer:
    def load(self):
        """Load face assets from disk."""
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
        pass

    def draw(self, state: str):
        """Draw the next frame for a face state."""
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
        #
        # Expected return value:
        # Nothing. The result appears on the display.
        pass
