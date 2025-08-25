# Prompt Engineering Basics Demo (Safe)
# This is a toy example, no external API calls.

examples = {
    "Instruction style": "Summarize: The sun is a star that gives Earth light and heat.",
    "Role prompting": "You are a teacher. Explain photosynthesis in simple terms.",
    "Few-shot": """Translate English to French:
    - Hello -> Bonjour
    - Good morning -> Bonjour
    - Thank you -> Merci
    Translate: Good night ->"""
}

for style, prompt in examples.items():
    print(f"\n=== {style} ===")
    print(prompt)
    print("Expected: Model would adjust style/response accordingly.\n")
