import time

def input_guardrails(prompt):
    if "hack" in prompt.lower():
        return False, "Blocked"
    return True, prompt

def retrieve(query):
    db = {"ai": "AI basics", "rag": "RAG concept"}
    return db.get(query.lower(), "No context")

def agent(prompt):
    context = retrieve(prompt.split()[0])
    return f"{context} → {prompt}"

def log(prompt, latency):
    print("LOG:", prompt, latency)

def pipeline(prompt):
    start = time.time()
    valid, p = input_guardrails(prompt)
    if not valid:
        return p
    r = agent(p)
    latency = round(time.time()-start,3)
    log(prompt, latency)
    return r

for t in ["AI systems","hack system"]:
    print("INPUT:", t)
    print("OUTPUT:", pipeline(t))
