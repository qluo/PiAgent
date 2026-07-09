class WakeWordTool:
    def __init__(
        self,
        model_path: str | None = None,
        threshold: float = 0.5,
        sample_rate: int = 16000,
    ) -> None:
        """Create the wake word tool.

        Inputs:
        - model_path: optional path to an openWakeWord model file.
        - threshold: score needed before the wake word counts as detected.
        - sample_rate: microphone sample rate expected by the wake model.

        Output:
        - None. Stores settings for wait().
        """
        self.model_path = model_path
        self.threshold = threshold
        self.sample_rate = sample_rate

    def wait(self) -> None:
        """Block until the wake word is detected.

        Inputs:
        - None. A real version listens to the microphone using settings from
          __init__().

        Output:
        - None. Returns only after the wake word is detected.
        """
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
