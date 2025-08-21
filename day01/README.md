# Day 1 — What is Generative AI vs Agentic AI?

**Series:** GenAI / Agentic AI — 30 Days (Public, Safe, Non-Company Project)  
**Branding:** © 2025 T S Narayana Reddy • CloudByteHub.ai  
**License:** MIT (see `LICENSE`).  
**Disclaimer:** Independent personal project. Not created for, by, or on behalf of any employer. No proprietary/sensitive data.

## Goals
- Clarify the difference between **Generative AI** and **Agentic AI**.
- Provide tiny, safe demos: a micro **text generator** and a **tool-using agent**.
- Establish conventions for the series (structure, licensing, branding).

## Concepts
- **Generative AI:** models that *generate* content from patterns (e.g., text, images, code).  
- **Agentic AI:** systems that *decide & act* toward goals, often using tools, memory, and planning.

### Key Differences
- **Primary Capability:** Generation vs. Goal-directed action.
- **Architecture:** Model-centric vs. Orchestrated components (planner, tools, memory).
- **I/O:** Prompt → Output vs. Perception → Reasoning → Tool use → Feedback → Action.
- **Evaluation:** Quality/faithfulness vs. Task success rate/latency/cost/safety.

## Demos (toy, offline, safe)
- `tiny_textgen.py` → template/Markov-style text generator (no external API).  
- `tiny_agent.py` → rule-based tool-using agent (calculator + small facts).

### Run locally
```bash
python tiny_textgen.py
python tiny_agent.py
```

.
