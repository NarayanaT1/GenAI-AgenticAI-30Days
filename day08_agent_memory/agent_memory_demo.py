# Day 8 — Agent with Memory (Chat History)
# Safe toy example

class MemoryAgent:
    def __init__(self):
        self.history = []

    def respond(self, user_input: str) -> str:
        self.history.append(("User", user_input))

        response = "I'm not sure how to respond to that."

        if "name is" in user_input.lower():
            name = user_input.split("name is")[-1].strip()
            response = f"Nice to meet you, {name}."
            self.history.append(("Agent", response))
            return response

        if "my name" in user_input.lower():
            for speaker, text in reversed(self.history):
                if speaker == "User" and "name is" in text.lower():
                    name = text.split("name is")[-1].strip()
                    response = f"You said your name is {name}."
                    self.history.append(("Agent", response))
                    return response

        if self.history:
            response = f"You said: '{user_input}'. Earlier we talked about {len(self.history)//2} turns."
        self.history.append(("Agent", response))
        return response

if __name__ == "__main__":
    agent = MemoryAgent()
    print("=== Day 8 — Agent with Memory (Chat History) ===")
    print("Type 'exit' to quit.")
    while True:
        q = input("You: ").strip()
        if q.lower() in ["exit", "quit"]:
            break
        print("Agent:", agent.respond(q))
