# Tiny, rule-based agent that uses tools (offline; safe demo).
import re

def tool_calc(expr: str) -> str:
    # Very small, safe calculator using Python eval on digits/operators only
    if not re.fullmatch(r"[0-9+\-*/(). ]+", expr):
        return "Error: unsupported characters"
    try:
        return str(eval(expr, {'__builtins__': {}}, {}))
    except Exception as e:
        return f"Error: {e}"

FACTS = {
    "generative ai": "Models that synthesize content (text/images/code) from learned patterns.",
    "agentic ai": "Systems that plan, choose tools, and act to accomplish goals."
}

def tool_facts(q: str) -> str:
    ql = q.lower()
    for k, v in FACTS.items():
        if k in ql:
            return v
    return "I don't have a fact for that, try a simple math expression or ask about generative/agentic AI."

TOOLS = {
    "calc": tool_calc,
    "facts": tool_facts,
}

def route(question: str) -> str:
    # Very naive routing: math → calc, otherwise → facts
    if re.search(r"[0-9][0-9+\-*/(). ]+", question):
        return "calc"
    return "facts"

def agent(question: str) -> str:
    tool = route(question)
    result = TOOLS[tool](question)
    return f"[tool={tool}] {result}"

if __name__ == "__main__":
    print(agent("What is agentic AI?"))
    print(agent("2 * (3 + 4)"))
