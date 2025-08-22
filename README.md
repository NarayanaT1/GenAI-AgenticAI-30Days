# Day 2 — Simple Text Generator with Hugging Face Transformers

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer. No proprietary/sensitive data.

This day shows how to build a tiny **text generator** using the Hugging Face `transformers` library
with a small open model (`distilgpt2`). It’s a **learning demo** only, kept simple and safe.

## Setup

Create a fresh virtual environment (recommended) and install dependencies:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install --upgrade pip
pip install transformers>=4.40 torch --quiet
```

> Note: The first run will download a small model (~80–100 MB). It will then be cached locally for offline use.

## Run

```bash
python textgen_transformers.py --prompt "Write a short note about agentic AI"
```

Optional knobs:
```bash
python textgen_transformers.py --prompt "Explain embeddings in 1 paragraph" --max_new_tokens 80 --temperature 0.7 --top_p 0.95 --seed 123
```

## Offline / Caching Tips

- After the first download, models are cached (typically at `~/.cache/huggingface` on Linux/macOS or `%USERPROFILE%\.cache\huggingface` on Windows).
- To force offline mode once cached:
  - PowerShell (Windows): `setx HF_HUB_OFFLINE 1`
  - Bash (Linux/macOS): `export HF_HUB_OFFLINE=1`

## File Overview

- `textgen_transformers.py` — minimal text-generation script with CLI arguments.
- `LICENSE` — MIT license.
- `README.md` — this file.

## Safety & Scope
- No external secrets, keys, or private data.
- Educational code only; not production-grade.
