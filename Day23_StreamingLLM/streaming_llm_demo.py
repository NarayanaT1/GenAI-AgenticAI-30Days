import time

def fake_llm_response(prompt):
    response = "Streaming responses improve user experience by sending tokens in real time."
    for token in response.split():
        yield token
        time.sleep(0.25)

def stream_answer(prompt):
    print("User:", prompt)
    print("Assistant:", end=" ", flush=True)

    for token in fake_llm_response(prompt):
        print(token, end=" ", flush=True)

    print("\n")

stream_answer("Explain streaming responses in LLMs")
