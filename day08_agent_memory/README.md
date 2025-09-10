# Day 8 — Memory in Agents (Chat History)

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer.

## Overview
Agents become much more useful when they **remember past interactions**.  
This demo shows a simple conversational agent with chat history.

## How it works
- The agent maintains a `history` list.
- Each user query and agent response is appended.
- When generating a new response, the agent checks the history for context.

## Example
```
You: My name is Narayana
Agent: Nice to meet you, Narayana.
You: What’s my name?
Agent: You said your name is Narayana.
```

## Files
- `agent_memory_demo.py` — toy conversational agent with memory.
- `README.md` — explanation file.
- `LICENSE` — MIT license.

## Run
```bash
python agent_memory_demo.py
```
