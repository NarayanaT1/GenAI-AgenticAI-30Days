# Day 3 — Tokenization Explained (Byte Pair Encoding Demo)

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer. No proprietary/sensitive data.

## Overview
Tokenization is the process of breaking down text into smaller units (tokens). LLMs like GPT use tokens instead of raw text.  
**Byte Pair Encoding (BPE)** is a popular algorithm that merges frequent pairs of symbols to build a compact vocabulary.

## Key Concepts
- Start with characters as tokens.
- Find the most frequent pair of tokens.
- Merge them into a new token.
- Repeat until desired vocabulary size.

## Demo Script
We provide `bpe_demo.py` — a toy implementation of BPE.

### Run
```bash
python bpe_demo.py
```

### Example Output
```
Merging: ('e', 'r')
[['low', '</w>'], ['low', 'er', '</w>'], ['low', 'est', '</w>'], ...]
```

## Educational Scope
- Safe toy example — no external libraries required (only Python standard lib).  
- Demonstrates how text compression ideas inspire LLM tokenization.

## Files
- `bpe_demo.py` — toy BPE implementation with step-by-step merges.
- `README.md` — this explanation file.
- `LICENSE` — MIT license.
