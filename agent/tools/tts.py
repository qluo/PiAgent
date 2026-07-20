import subprocess


class TextToSpeechTool:
    def __init__(
        self,
        voice_model_path: str = "models/piper/en_US-lessac-low.onnx",
        piper_binary: str = "tools/piper/piper",
        player_binary: str = "aplay",
        sample_rate: int = 22050,
    ) -> None:
        """Create the text-to-speech tool.

        Inputs:
        - voice_model_path: path to a local Piper voice model.
        - piper_binary: path or command name for the Piper program.
        - player_binary: path or command name for the audio player.
        - sample_rate: audio sample rate expected by the Piper voice.

        Output:
        - None. Stores settings for speak().
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
        # Real version idea:
        # 1. Send text into Piper.
        # 2. Ask Piper for raw audio with --output-raw.
        # 3. Pipe Piper's raw audio directly into aplay.
        #
        # Expected return value:
        # Nothing. This method finishes after speaking is done.
        # Piper reads text from stdin and writes raw speech audio to stdout.
        # aplay reads that raw audio from stdin and sends it to the speaker.
        #
        # TODO for students:
        # 1. Start piper with subprocess.Popen(...).
        # 2. Send text into piper stdin.
        # 3. Pipe piper stdout into aplay stdin, without saving a WAV file.
        # 4. Wait for both programs to finish.
        
        # Piper reads text from stdin and writes raw speech audio to stdout.
        # We use --output-raw so the audio can go straight to the speaker.
        piper = subprocess.Popen(
            [
                self.piper_binary,
                "--model",
                self.voice_model_path,
                "--output-raw",
            ],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )

        # aplay reads the raw audio from Piper and sends it to the speaker.
        # These settings match Piper's common 16-bit mono output format.
        player = subprocess.Popen(
            [
                self.player_binary,
                "-r",
                str(self.sample_rate),
                "-f",
                "S16_LE",
                "-t",
                "raw",
                "-",
            ],
            stdin=piper.stdout,
        )

        # Close our extra copy of Piper's stdout so aplay knows when audio ends.
        #if piper.stdout is not None:
        #    piper.stdout.close()

        # Send the sentence to Piper, then wait for speech generation and playback.
        if piper.stdin is not None:
            piper.stdin.write(text.encode("utf-8"))
            piper.stdin.close()

        piper.wait()
        player.wait()
