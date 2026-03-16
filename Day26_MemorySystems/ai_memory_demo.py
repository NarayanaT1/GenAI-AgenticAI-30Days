# Day 26 – AI Memory Systems Demo

short_term_memory = []

long_term_memory = {
    "ai": "Artificial Intelligence allows machines to simulate human intelligence.",
    "rag": "Retrieval Augmented Generation combines search with generation.",
    "agent": "AI agents can plan tasks and use tools."
}

def retrieve_long_term(query):
    return long_term_memory.get(query.lower(), "No stored knowledge found")

def agent(prompt):
    
    # store conversation
    short_term_memory.append(prompt)

    words = prompt.split()
    knowledge = retrieve_long_term(words[-1])

    response = f"Context: {short_term_memory[-3:]}\nKnowledge: {knowledge}"

    return response

tests = [
    "Tell me about ai",
    "Explain rag",
    "What is an agent"
]

for t in tests:
    print("User:", t)
    print("Agent:", agent(t))
    print()
