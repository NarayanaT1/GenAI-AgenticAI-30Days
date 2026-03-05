import time

# Simulated LLM call
def call_llm(prompt):
    time.sleep(0.5)  # simulate latency
    return "Generated response for: " + prompt

def estimate_tokens(text):
    return len(text.split())

def estimate_cost(tokens):
    price_per_1k_tokens = 0.002
    return tokens / 1000 * price_per_1k_tokens

prompt = "Explain observability in AI systems"

start = time.time()
response = call_llm(prompt)
end = time.time()

latency = end - start
tokens = estimate_tokens(response)
cost = estimate_cost(tokens)

print("Response:", response)
print("Latency (seconds):", latency)
print("Estimated tokens:", tokens)
print("Estimated cost ($):", cost)
