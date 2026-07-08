class TextToSpeechTool:
    def speak(self, text: str):
        """Speak text aloud."""
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
