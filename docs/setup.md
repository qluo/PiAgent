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

Run the fake working demo:

```bash
python3 demo.py
```

## Run Lesson Tests

Run tests from the project folder, the folder that contains `demo.py`, `face/`,
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

## Ollama Setup

Install Ollama using the official instructions:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull a small local model:

```bash
ollama pull llama3.2:1b
```
