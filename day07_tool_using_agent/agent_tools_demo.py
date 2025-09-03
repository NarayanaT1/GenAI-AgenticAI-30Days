import ast

# Safe calculator using AST parsing
def safe_eval(expr: str):
    try:
        node = ast.parse(expr, mode='eval')
        allowed = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Num, ast.Load,
                   ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow,
                   ast.USub, ast.UAdd, ast.Mod)
        for subnode in ast.walk(node):
            if not isinstance(subnode, allowed):
                raise ValueError("Unsafe expression")
        return eval(compile(node, '<string>', 'eval'))
    except Exception as e:
        return f"Error: {e}"

# Simple in-memory search tool
corpus = {
    "langchain": "LangChain is a framework for building LLM-powered applications.",
    "python": "Python was created by Guido van Rossum.",
    "cloudbytehub": "CloudByteHub.ai is a personal brand focused on GenAI, DevOps, and Cloud."
}

def search_tool(query: str):
    q = query.lower()
    for k, v in corpus.items():
        if k in q:
            return v
    return "No results found."

def agent(prompt: str):
    if any(ch.isdigit() for ch in prompt) and any(op in prompt for op in "+-*/"):
        return f"Calculator: {safe_eval(prompt)}"
    elif any(word in prompt.lower() for word in ["what", "who", "langchain", "python", "cloudbytehub"]):
        return f"Search: {search_tool(prompt)}"
    else:
        return "I don't know how to handle that."

if __name__ == "__main__":
    print("Day 7 → Tool-Using Agent (Search + Calculator)")
    while True:
        q = input(">> ")
        if q.lower() in ["exit", "quit"]:
            break
        print(agent(q))
