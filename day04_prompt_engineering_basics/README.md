# Day 4 — Prompt Engineering Basics (Safe Text Prompts)

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer. No proprietary/sensitive data.

## Overview
Prompt engineering is the practice of designing effective inputs (prompts) to guide language model outputs.  
This day introduces **safe, educational basics** without using any external APIs.

## Why Prompts Matter
- Models generate text based on input instructions.  
- Well-structured prompts improve clarity, relevance, and consistency.  
- Prompt engineering is a key skill for working with GenAI systems.

## Safe Techniques
- **Instruction style** → clear, direct task.  
- **Role prompting** → assign a role to shape tone/explanation.  
- **Few-shot prompting** → provide examples to guide responses.

## Demo Script
We provide `prompt_basics.py` — a toy example showing different prompt styles.

### Run
```bash
python prompt_basics.py
```

### Example Output
```
=== Instruction style ===
Summarize: The sun is a star that gives Earth light and heat.
(Expected: A short summary)

=== Role prompting ===
You are a teacher. Explain photosynthesis in simple terms.
(Expected: A simple, teacher-like explanation)

=== Few-shot ===
Translate English to French:
- Hello -> Bonjour
- Good morning -> Bonjour
- Thank you -> Merci
Translate: Good night ->
(Expected: 'Bonne nuit')
```

## Files
- `prompt_basics.py` — toy examples of prompt styles.  
- `README.md` — this explanation file.  
- `LICENSE` — MIT license.  

