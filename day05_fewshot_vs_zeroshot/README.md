# Day 5 — Few-shot vs Zero-shot Prompting (Safe Demo)

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer. No proprietary/sensitive data.

## Overview
Prompting strategies change how language models perform tasks.  
- **Zero-shot prompting**: No examples provided. The model is expected to infer the task.  
- **Few-shot prompting**: A few examples are given to guide the model.  

## Why It Matters
- Zero-shot is flexible but sometimes less accurate.  
- Few-shot improves reliability for tasks like classification, translation, or structured output.  

## Demo Script
We provide `fewshot_vs_zeroshot.py` — a toy example showing safe, offline prompts.

### Run
```bash
python fewshot_vs_zeroshot.py
```

### Example Output
```
=== Zero-shot ===
Prompt: Translate 'Good night' to French
(Expected: Bonne nuit)

=== Few-shot ===
Translate English to French:
- Hello -> Bonjour
- Thank you -> Merci
- Good morning -> Bonjour
Translate: Good night ->
(Expected: Bonne nuit)
```

## Files
- `fewshot_vs_zeroshot.py` — toy prompt comparison.  
- `README.md` — this explanation file.  
- `LICENSE` — MIT license.  
