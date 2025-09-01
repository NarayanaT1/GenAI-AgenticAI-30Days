# Day 6 — LangChain Intro: Chaining Two Tools Together

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer. No proprietary/sensitive data.

## Overview
LangChain is a framework for building applications with language models by **chaining tools and steps together**.  
This day introduces a simple **toy chain** to demonstrate the concept.

## Why Chaining Matters
- Breaks complex tasks into smaller steps.  
- Encourages modular, reusable tools.  
- Makes workflows transparent and easier to debug.  

## Demo Script
We provide `langchain_chain_demo.py` — a toy example chaining two safe tools.  

### Run
```bash
python langchain_chain_demo.py
```

### Example Output
```
=== LangChain Toy Chain Demo ===
Step 1 (Math Tool): 12
Step 2 (Formatter Tool): The computed result is 12.
```

## Files
- `langchain_chain_demo.py` — toy chain demo.  
- `README.md` — this explanation file.  
- `LICENSE` — MIT license.  
