# Day 11 — Embeddings + Vector DB Basics (FAISS-style)
import numpy as np
import re

def tokenize(text):
    return re.findall(r"[a-z0-9]+", text.lower())

def hash_embed(text, dim=256):
    v = np.zeros(dim, dtype=np.float32)
    for tok in tokenize(text):
        v[hash(tok) % dim] += 1.0
    n = np.linalg.norm(v) + 1e-8
    return v / n

class SimpleVectorIndex:
    def __init__(self, dim=256):
        self.dim = dim
        self.vectors = None
        self.texts = []

    def add(self, texts):
        embs = np.vstack([hash_embed(t, self.dim) for t in texts])
        self.vectors = embs if self.vectors is None else np.vstack([self.vectors, embs])
        self.texts.extend(texts)

    def search(self, query, k=3):
        q = hash_embed(query, self.dim)
        sims = self.vectors @ q
        idxs = np.argsort(-sims)[:k]
        return [(self.texts[i], float(sims[i])) for i in idxs]

if __name__ == '__main__':
    corpus = [
        'Paris is the capital of France.',
        'Puppies are young dogs and are very cute.',
        'Neural networks are a subset of machine learning.',
        'The Eiffel Tower is located in Paris.',
        'Cats are independent pets.',
        'Reinforcement learning uses rewards to train agents.'
    ]
    idx = SimpleVectorIndex()
    idx.add(corpus)

    print('=== Day 11 — Embeddings + Vector DB (FAISS-style) ===')
    print(\"Type a query (or 'exit'). Try: 'puppy', 'capital of france', 'neural networks'\" )
    while True:
        q = input('\\nQuery: ').strip()
        if q.lower() in ['exit', 'quit']:
            break
        for t, s in idx.search(q, k=3):
            print(f'  -> {s:.3f} | {t}')
