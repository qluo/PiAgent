DEFAULT_WAKE_WORD_MODEL = "hey_jarvis"
CHUNK_SIZE = 1280


class WakeWordTool:
    def __init__(
        self,
        model_path: str | None = DEFAULT_WAKE_WORD_MODEL,
        threshold: float = 0.5,
        sample_rate: int = 16000,
        mode: str = "microphone",
    ) -> None:
        """Create the wake word tool.

        Inputs:
        - model_path: optional path to an openWakeWord model file.
        - threshold: score needed before the wake word counts as detected.
        - sample_rate: microphone sample rate expected by the wake model.
        - mode: "keyboard" for the classroom/test version or "microphone" for
          live Raspberry Pi audio. It defaults to "microphone" for the real
          assistant.

        Output:
        - None. Stores settings for wait().
        """
        self.model_path = model_path
        self.threshold = threshold
        self.sample_rate = sample_rate
        self.mode = mode

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
        # Lesson 3 helper functions:
        # - For keyboard practice, call self._wait_for_keyboard_wake().
        # - For the Raspberry Pi version, call self._wait_for_microphone_wake().
        # - Use self.mode to choose between "keyboard" and "microphone".
        pass

    def _wait_for_keyboard_wake(self) -> None:
        """Teaching helper: wait until someone types wake."""
        # TODO for students:
        # 1. Keep asking for input().
        # 2. Return when the typed word is "wake".
        pass

    def _wait_for_microphone_wake(self) -> None:
        """Listen to microphone audio and check openWakeWord scores."""
        # TODO for students:
        # 1. Load the openWakeWord Model.
        # 2. Create audio_queue = Queue().
        # 3. Make audio_callback(indata, _frames, _time, status). Inside it, add
        #    one mono audio chunk with audio_queue.put(indata[:, 0].copy()).
        # 4. Open sd.InputStream(..., callback=audio_callback).
        # 5. In a loop, score each chunk with model.predict(audio_chunk).
        # 6. Return when max(scores.values()) reaches self.threshold.
        pass
