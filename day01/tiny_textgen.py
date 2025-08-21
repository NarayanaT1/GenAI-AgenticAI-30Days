# Tiny, offline text generator (no external APIs; safe demo).
import random

CORPUS = [
    "Generative AI creates text by predicting likely next tokens.",
    "Agentic AI chooses actions and tools to achieve goals.",
    "Embeddings help connect semantic meaning to retrieval."
]

TEMPLATES = [
    "Today we explore {topic}. In short, {line}",
    "Quick note on {topic}: {line} This illustrates the basics.",
    "TL;DR on {topic} — {line}"
]

TOPICS = ["Generative AI", "Agentic AI", "Embeddings", "Prompting"]

def sample_line():
    # Pick a random sentence from the corpus
    return random.choice(CORPUS)

def generate_text(topic=None):
    topic = topic or random.choice(TOPICS)
    tpl = random.choice(TEMPLATES)
    return tpl.format(topic=topic, line=sample_line())

if __name__ == "__main__":
    for _ in range(3):
        print(generate_text())
