def calculator(input_text):
    try:
        return eval(input_text)
    except:
        return "Invalid calculation"

def search(input_text):
    knowledge = {
        "ai": "Artificial Intelligence enables machines to simulate human intelligence.",
        "rag": "RAG combines retrieval with generation.",
        "agent": "Agents can dynamically select tools."
    }
    return knowledge.get(input_text.lower(), "No data found")

tool_registry = {
    "calculator": calculator,
    "search": search
}

def select_tool(prompt):
    if "calculate" in prompt.lower():
        return "calculator"
    if "search" in prompt.lower():
        return "search"
    return None

def agent(prompt):
    tool_name = select_tool(prompt)

    if tool_name and tool_name in tool_registry:
        tool = tool_registry[tool_name]

        if tool_name == "calculator":
            input_text = prompt.lower().replace("calculate", "").strip()
        else:
            input_text = prompt.lower().replace("search", "").strip()

        result = tool(input_text)
        return f"Tool Used: {tool_name} → Result: {result}"

    return "No suitable tool found"

tests = ["calculate 10*5", "search ai", "search rag"]

for t in tests:
    print("INPUT:", t)
    print("OUTPUT:", agent(t))
    print()
