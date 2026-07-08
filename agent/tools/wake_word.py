class WakeWordTool:
    def wait(self):
        """Block until the wake word is detected."""
        # Lesson 3: Wake Word Detection
        #
        # Goal:
        # Pause here until the assistant should wake up.
        #
        # Suggested packages:
        # - openwakeword: detects wake words from microphone audio.
        # - sounddevice: records microphone audio in Python.
        # - numpy<2: audio arrays used by openwakeword.
        #
        # Small first step:
        # Do a keyboard version before real audio:
        # keep asking for input until the user types "wake".
        #
        # Real version idea:
        # 1. Open the microphone with sounddevice.
        # 2. Feed short chunks of audio into openwakeword.
        # 3. Return from this method only when the wake score is high enough.
        #
        # Expected return value:
        # Nothing. This method returns only when the wake word is detected.
        pass
