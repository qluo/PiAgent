class TextToSpeechTool:
    def __init__(
        self,
        voice_model_path: str | None = None,
        output_wav: str = "output.wav",
    ) -> None:
        """Create the text-to-speech tool.

        Inputs:
        - voice_model_path: optional path to a local TTS voice model.
        - output_wav: path where generated speech audio can be saved.

        Output:
        - None. Stores settings for speak().
        """
        self.voice_model_path = voice_model_path
        self.output_wav = output_wav

    def speak(self, text: str) -> None:
        """Speak text aloud.

        Inputs:
        - text: the sentence the agent should say.

        Output:
        - None. Returns after speaking or printing is finished.
        """
        # Lesson 6: Text-To-Speech
        #
        # Goal:
        # Turn the agent's response text into spoken audio.
        #
        # Suggested tools:
        # - Piper: local text-to-speech that can run on Raspberry Pi.
        # - aplay: simple WAV playback command on Raspberry Pi OS.
        #
        # Small first step:
        # Print the text first:
        #   print(f"Agent: {text}")
        # Then replace the print with real speech after the loop works.
        #
        # Real version idea:
        # 1. Send text into Piper.
        # 2. Save speech as output.wav.
        # 3. Play output.wav with aplay.
        #
        # Expected return value:
        # Nothing. This method finishes after speaking is done.
        pass
