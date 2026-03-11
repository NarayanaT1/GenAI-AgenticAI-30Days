from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "AI agents can use tools to perform tasks.",
    "Vector databases store embeddings for similarity search.",
    "Retrieval Augmented Generation improves factual accuracy."
]

def embed(text):
    return np.array([len(text), text.count(" "), text.count("a")])

doc_vectors = [embed(d) for d in documents]

def vector_search(query):
    q_vec = embed(query)
    scores = cosine_similarity([q_vec], doc_vectors)[0]
    return documents[np.argmax(scores)]

def rag_agent(question):
    context = vector_search(question)
    return f"Using context: {context}\nAnswer: {question}"

questions = ["What is a vector database?", "Explain AI agents"]

for q in questions:
    print("QUESTION:", q)
    print(rag_agent(q))
    print()
