architecture = {
    "User Layer": "Web app, mobile app, chatbot UI, or API consumers",
    "Gateway/API Layer": "Authentication, routing, rate limiting",
    "Orchestration Layer": "Planner, tool selection, workflow control",
    "Retrieval Layer": "Vector DB, keyword search, document store",
    "Model Layer": "LLM inference, prompts, response generation",
    "Safety Layer": "Guardrails, policy filters, prompt injection defense",
    "Observability Layer": "Latency, token usage, logs, alerts, dashboards"
}

def print_architecture():
    print("=== Day 25 – Production AI Architecture Overview ===")
    for layer, desc in architecture.items():
        print(f"{layer}: {desc}")

if __name__ == "__main__":
    print_architecture()
