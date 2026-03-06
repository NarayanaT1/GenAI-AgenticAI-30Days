# Simple Tool-Using AI Agent Demo

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "Invalid expression"

def search_knowledge(query):

    knowledge_base = {
        "python": "Python is a popular programming language.",
        "llm": "Large Language Models generate text using deep learning.",
        "agent": "AI agents can use tools to complete tasks."
    }

    return knowledge_base.get(query.lower(), "No knowledge found")

def agent(prompt):

    if "calculate" in prompt.lower():
        expr = prompt.lower().replace("calculate", "").strip()
        return calculator(expr)

    if "search" in prompt.lower():
        q = prompt.lower().replace("search", "").strip()
        return search_knowledge(q)

    return "Agent could not determine tool"

tests = [
    "calculate 5*7",
    "search python",
    "search llm",
    "calculate 100/5"
]

for t in tests:
    print("INPUT:", t)
    print("OUTPUT:", agent(t))
    print()
