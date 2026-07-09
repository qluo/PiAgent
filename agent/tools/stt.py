class SpeechToTextTool:
    def __init__(
        self,
        sample_rate: int = 16000,
        seconds: float = 3.0,
        output_wav: str = "input.wav",
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
        self.output_wav = output_wav

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
        # Record a fixed 3-second audio clip and save it as input.wav.
        # Do this before trying silence detection or streaming audio.
        #
        # Real version idea:
        # 1. Record audio with sounddevice.rec(...).
        # 2. Save it as a WAV file.
        # 3. Run whisper.cpp on the WAV file.
        # 4. Read the transcription text.
        #
        # Expected return value:
        # The user's words as a Python string.
        return ""
