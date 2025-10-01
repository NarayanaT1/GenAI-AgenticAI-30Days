# Day 10 — Planner/Executor Pattern

**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not affiliated with any employer.

## Overview
The **Planner/Executor** pattern splits a problem into two roles:
- **Planner**: Break a high‑level objective into ordered steps.
- **Executor**: Perform the steps one by one, reporting progress and results.

This toy demo uses a safe offline script (no external APIs).

## How it works
1. Provide a high‑level task (e.g., "Plan a weekend trip").  
2. The Planner generates a structured checklist.  
3. The Executor simulates each step and logs completion.  
4. A simple **Supervisor** collects a transcript.

## Run
```bash
python planner_executor_demo.py
```
Try editing the `TASK` variable or the `PLAN_TEMPLATES` for different flows.

## Files
- `planner_executor_demo.py` — toy Planner/Executor example.
- `README.md` — explanation file.
- `LICENSE` — MIT license.
