# Setup

## Create A Virtual Environment With uv

Install `uv` first if you do not already have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create and activate a virtual environment:

```bash
uv venv
source .venv/bin/activate
```

Install the Python packages:

```bash
uv pip install -r requirements.txt
```

Run the fake working Lesson 1 demo:

```bash
uv run python demos/lesson1_demo.py
```

## Run Lesson Tests

Run tests from the project folder, the folder that contains `demos/`, `face/`,
`agent/`, and `pytest.ini`.

Each lesson has its own test folder. Run one small test at a time while you build.
For example, in Lesson 2 you can test `FaceState`, then `FaceRenderer.load()`, then
`FaceRenderer.draw()`:

```bash
uv run pytest tests/lesson_2/test_01_face_state.py
uv run pytest tests/lesson_2/test_03_renderer_load.py
uv run pytest tests/lesson_2/test_04_renderer_draw.py
```

Run a whole lesson folder when you think the lesson is complete:

```bash
uv run pytest tests/lesson_1
uv run pytest tests/lesson_2
uv run pytest tests/lesson_3
uv run pytest tests/lesson_4
uv run pytest tests/lesson_5
uv run pytest tests/lesson_6
uv run pytest tests/lesson_7
uv run pytest tests/lesson_8
uv run pytest tests/lesson_9
```

It is normal for later lesson tests to fail before you implement those lessons.

## Tool Settings

Some skeleton classes have an `__init__()` method that stores settings before
the real implementation is written. For example:

```python
WakeWordTool(threshold=0.5, sample_rate=16000)
SpeechToTextTool(seconds=3.0, output_wav="input.wav")
TextToSpeechTool(output_wav="output.wav")
SearchTool(max_results=1, region="us-en")
FaceRenderer(faces_dir="faces")
```

Students can keep the defaults at first, then change one setting at a time
when testing real hardware.

## Run The Wake Word Audio Demo

Lesson 3 also has a manual microphone demo. This is not a unit test because it
needs real hardware:

```bash
uv run python demos/test_wake_word_audio.py
```

If detection is too hard, try a lower threshold:

```bash
uv run python demos/test_wake_word_audio.py --threshold 0.3
```

## Ollama Setup

Install Ollama using the official instructions:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull a small local model:

```bash
ollama pull llama3.2:1b
```
