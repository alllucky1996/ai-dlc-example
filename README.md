# ai-dlc-example

A practice project demonstrating how to integrate AI into your development lifecycle (AI DLC).

## Features

- **Code Review** – get AI-generated feedback on your source code
- **Documentation Generation** – automatically generate docstrings and docs for functions/classes
- **Extensible client** – a thin wrapper around OpenAI-compatible APIs that can be pointed at any compatible endpoint

## Project Structure

```
ai-dlc-example/
├── src/
│   └── ai_dlc/
│       ├── __init__.py        # Package exports
│       ├── client.py          # AI API client
│       ├── code_reviewer.py   # AI code review helper
│       └── doc_generator.py   # AI documentation generator
├── tests/
│   ├── test_client.py
│   ├── test_code_reviewer.py
│   └── test_doc_generator.py
├── examples/
│   ├── code_review_example.py
│   └── doc_generation_example.py
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Set your API key

```bash
export AI_API_KEY=your_openai_api_key
```

### 3. Run an example

```bash
python examples/code_review_example.py
```

## Configuration

| Environment Variable | Default | Description |
|---|---|---|
| `AI_API_KEY` | _(required)_ | Your OpenAI (or compatible) API key |
| `AI_MODEL` | `gpt-3.5-turbo` | Model name to use |
| `AI_BASE_URL` | `https://api.openai.com/v1` | API base URL (override for other providers) |

## Usage

```python
from ai_dlc import AIClient, CodeReviewer, DocGenerator

client = AIClient(api_key="your-key")

# Review code
reviewer = CodeReviewer(client=client)
feedback = reviewer.review(open("my_script.py").read(), language="python")
print(feedback)

# Generate documentation
generator = DocGenerator(client=client)
docs = generator.generate(open("my_module.py").read(), language="python")
print(docs)
```

## Running Tests

```bash
pip install pytest
pytest tests/
```
