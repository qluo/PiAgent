class SpeechToTextTool:
    def __init__(
        self,
        sample_rate: int = 16000,
        seconds: float = 10.0,
        silence_seconds: float = 0.9,
        silence_threshold: int = 500,
        model_path: str = "models/whisper/ggml-base.en.bin",
        whisper_binary: str = "whisper.cpp/build/bin/whisper-cli",
        mode: str = "microphone",
    ) -> None:
        """Create the speech-to-text tool.

        Inputs:
        - sample_rate: microphone sample rate for recording.
        - seconds: starting recording length for the first version.
        - output_wav: path where recorded audio can be saved.

        Output:
        - None. Stores settings for listen_and_transcribe().
        """
        self.sample_rate = sample_rate
        self.seconds = seconds
        self.silence_seconds = silence_seconds
        self.silence_threshold = silence_threshold
        self.model_path = model_path
        self.whisper_binary = whisper_binary
        self.mode = mode

    def listen_and_transcribe(self) -> str:
        """Capture user speech and return transcribed text.

        Inputs:
        - None. A real version records audio using settings from __init__().

        Output:
        - The user's words as a string.
        """
        # Lesson 5: Speech-To-Text
        #
        # Goal:
        # Record the user's voice and turn it into text.
        #
        # Suggested packages/tools:
        # - sounddevice: record audio from the microphone.
        # - numpy<2: stores recorded audio arrays.
        # - wave: built-in Python module for saving WAV files.
        # - whisper.cpp: local speech-to-text program for transcription.
        #
        # Small first step:
        # If self.mode is "keyboard", return input("You: ") so the rest of the
        # agent can be tested before the microphone works.
        #
        # Real version idea:
        # 1. Call self.listen_until_silence() to capture one spoken question.
        # 2. Inside listen_until_silence(), call self.loudness(audio_chunk) to
        #    decide when speech starts and when silence has lasted long enough.
        # 3. Save the recorded audio bytes as a temporary WAV file.
        # 4. Run whisper.cpp using self.whisper_binary and self.model_path.
        # 5. Return the transcription text from whisper.cpp.
        #
        # Expected return value:
        # The user's words as a Python string.
        return ""

    def listen_until_silence(self) -> bytes:
        """Record when speech starts, then stop after a short silence."""
        # TODO for students:
        # 1. Open the microphone with sounddevice.
        # 2. Start saving audio chunks when loudness() says speech began.
        # 3. Stop after a short silence.
        # 4. Return the recorded audio bytes.
        return b""

    def loudness(self, audio_bytes: bytes) -> float:
        """Return a simple average volume for 16-bit microphone audio."""
        # TODO for students:
        # 1. Convert audio_bytes into 16-bit samples.
        # 2. Return the average absolute sample value.
        return 0.0
