# Day 13 — Chunking Strategies & Evaluation (Toy, offline)
"
import os, re, numpy as np

try:
    import PyPDF2
except Exception:
    PyPDF2 = None

PDF_FILE = "sample.pdf"
QUERY = "How does chunking help RAG?"

def read_pdf_text(path):
    if PyPDF2 is None:
        return ""
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return "\n".join([p.extract_text() or "" for p in reader.pages])
    except Exception:
        return ""

def fallback_text():
    return "AI text about NLP, CV, ML, RAG and chunking strategies."

def tokenize(t):
    return re.findall(r"[a-z0-9]+", t.lower())

def hash_embed(text, dim=256):
    v = np.zeros(dim, dtype=np.float32)
    for tok in tokenize(text):
        v[hash(tok)%dim]+=1
    n = np.linalg.norm(v)+1e-8
    return v/n

def chunk_fixed(text, size=50):
    w=text.split();return [" ".join(w[i:i+size]) for i in range(0,len(w),size)]

def chunk_sliding(text, size=60, overlap=25):
    w=text.split();res=[];i=0;step=max(1,size-overlap)
    while i<len(w):
        res.append(" ".join(w[i:i+size])); i+=step
    return res

def chunk_semantic(text):
    paras=[p.strip() for p in text.splitlines() if p.strip()]
    return paras if paras else chunk_fixed(text,80)

def build_index(chunks, dim=256):
    embs=[hash_embed(c,dim) for c in chunks]
    return np.vstack(embs), chunks

def topk(q, index, chunks, k=2):
    qv=hash_embed(q); sims=index@qv; idxs=np.argsort(-sims)[:k]
    return [(chunks[i], float(sims[i])) for i in idxs]

def main():
    text = read_pdf_text(PDF_FILE) if os.path.exists(PDF_FILE) else ""
    if not text.strip(): text=fallback_text()
    strategies={
        "fixed": chunk_fixed(text,50),
        "sliding": chunk_sliding(text,60,25),
        "semantic": chunk_semantic(text),
    }
    print("=== Day 13 — Chunking Strategies & Evaluation ==="); print(f"Query: {QUERY}\n")
    for name,chunks in strategies.items():
        idx,chs=build_index(chunks); results=topk(QUERY,idx,chs,2)
        print(f"[{name}] top-2 hits:")
        for c,s in results:
            snip=(c[:160]+'...') if len(c)>160 else c
            print(f"  score={s:.3f} | {snip}")
        print()

if __name__=='__main__': main()
