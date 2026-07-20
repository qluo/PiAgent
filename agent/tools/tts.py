import subprocess


class TextToSpeechTool:
    def __init__(
        self,
        voice_model_path: str = "models/piper/en_US-lessac-low.onnx",
        piper_binary: str = "tools/piper/piper",
        player_binary: str = "aplay",
        sample_rate: int = 22050,
    ) -> None:
        """Store the settings used by :meth:`speak`.

        Args:
            voice_model_path: Local Piper voice model.
            piper_binary: Piper command that turns text into raw audio.
            player_binary: Audio-player command that sends raw audio to the speaker.
            sample_rate: Sample rate used by the voice and aplay.
        """
        self.voice_model_path = voice_model_path
        self.piper_binary = piper_binary
        self.player_binary = player_binary
        self.sample_rate = sample_rate

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
        # Implementation guide:
        # 1. Use subprocess.Popen() to start self.piper_binary with --model,
        #    self.voice_model_path, and --output-raw. Set stdin and stdout to
        #    subprocess.PIPE so Python can send text and receive raw audio.
        # 2. Start self.player_binary with -r self.sample_rate, -f S16_LE,
        #    -t raw, and -. Pass Piper's stdout as the player's stdin, so Piper
        #    streams its raw 16-bit mono audio directly to aplay.
        # 3. Encode text as UTF-8, write the bytes to Piper's stdin, then close
        #    that stdin to tell Piper that the complete sentence was sent.
        # 4. Wait for Piper and then the player. This prevents the next agent
        #    turn from starting while the current answer is still speaking.
        
        return
