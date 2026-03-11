# Multi‑Step AI Agent Demo

def planner(prompt):
    if "calculate" in prompt.lower():
        return "calculator"
    if "search" in prompt.lower():
        return "search"
    return "unknown"

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid calculation"

def search_tool(query):
    knowledge = {
        "ai": "Artificial Intelligence enables machines to simulate human intelligence.",
        "agent": "AI agents can plan, reason, and use tools.",
        "llm": "Large Language Models generate text using deep learning."
    }
    return knowledge.get(query.lower(), "No knowledge found")

def agent(prompt):

    tool = planner(prompt)

    if tool == "calculator":
        expr = prompt.lower().replace("calculate", "").strip()
        result = calculator(expr)

    elif tool == "search":
        query = prompt.lower().replace("search", "").strip()
        result = search_tool(query)

    else:
        result = "Agent could not determine a tool"

    return result


tests = [
    "calculate 12*5",
    "search ai",
    "search agent",
    "calculate 100/4"
]

for t in tests:
    print("INPUT:", t)
    print("OUTPUT:", agent(t))
    print()
