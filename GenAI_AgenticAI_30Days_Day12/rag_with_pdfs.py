import numpy as np
import PyPDF2

# Simple hash embedding for demo (toy)
def embed_text(text):
    return np.array([hash(word) % 1000 for word in text.split()])[:50]

# Load PDF
def load_pdf(file_path):
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + " "
        return text

# Split into chunks
def chunk_text(text, size=40):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]

# Build vector index (dict of embeddings)
def build_index(chunks):
    return [embed_text(chunk) for chunk in chunks]

# Simple cosine similarity
def cosine_sim(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10)

def search(query, chunks, index, top_k=2):
    q_vec = embed_text(query)
    sims = [cosine_sim(q_vec, vec) for vec in index]
    ranked = np.argsort(sims)[::-1][:top_k]
    return [chunks[i] for i in ranked]

if __name__ == "__main__":
    pdf_text = load_pdf("sample.pdf")
    chunks = chunk_text(pdf_text)
    index = build_index(chunks)

    query = "What is AI about?"
    results = search(query, chunks, index)
    print("Query:", query)
    print("Top results:")
    for r in results:
        print("-", r)
