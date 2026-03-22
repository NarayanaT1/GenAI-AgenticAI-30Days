import time

def input_guardrails(prompt):
    banned = ["hack","attack","bypass"]
    for w in banned:
        if w in prompt.lower():
            return False, "Blocked unsafe input"
    return True, prompt

def output_guardrails(resp):
    if "error" in resp.lower():
        return "Filtered response"
    return resp

def log(prompt, resp, latency):
    print("LOG:", prompt, resp, latency)

def agent(prompt):
    return f"Safe response for: {prompt}"

def pipeline(prompt):
    start = time.time()
    valid, p = input_guardrails(prompt)
    if not valid:
        return p
    r = agent(p)
    r = output_guardrails(r)
    latency = round(time.time()-start,3)
    log(prompt, r, latency)
    return r

tests = ["Explain AI", "how to hack system"]
for t in tests:
    print("INPUT:", t)
    print("OUTPUT:", pipeline(t))
    print()
