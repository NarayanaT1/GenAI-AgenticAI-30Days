# Day 28 – Workflow Orchestration Demo

import random

def planner(prompt):
    return "retrieve"

def retrieve_data(query):
    if random.random() < 0.5:
        raise Exception("Retrieval failed")
    return "Relevant context data"

def generate_response(context, prompt):
    return f"Using {context}, answering: {prompt}"

def fallback_response(prompt):
    return f"Fallback response for: {prompt}"

def workflow(prompt, retries=2):
    try:
        step = planner(prompt)

        for attempt in range(retries):
            try:
                context = retrieve_data(prompt)
                return generate_response(context, prompt)
            except Exception as e:
                print(f"Retry {attempt+1} due to error:", e)

        return fallback_response(prompt)

    except Exception:
        return fallback_response(prompt)


tests = ["Explain AI orchestration", "What is RAG?"]

for t in tests:
    print("INPUT:", t)
    print("OUTPUT:", workflow(t))
    print()
