import re, math, numpy as np
corpus=[
"Paris is the capital of France.",
"Puppies are young dogs and are very cute.",
"Neural networks are a subset of machine learning.",
"The Eiffel Tower is located in Paris.",
"Computer Vision interprets images and video to understand scenes.",
"Reinforcement learning uses rewards to train agents to act."
]
def tokenize(t): return re.findall(r"[a-z0-9]+", t.lower())
def build_tfidf(corpus):
    docs=[tokenize(t) for t in corpus]; df={}
    for d in docs:
        for term in set(d): df[term]=df.get(term,0)+1
    N=len(docs); idf={t: math.log((N+1)/(df[t]+1))+1.0 for t in df}
    tfidf=[]; 
    for d in docs:
        tf={}; 
        for t in d: tf[t]=tf.get(t,0)+1
        vec={t:(tf[t]/len(d))*idf.get(t,0.0) for t in tf}
        tfidf.append(vec)
    return tfidf,idf
def tfidf_score(q, tfidf_docs, idf):
    qtok=set(tokenize(q)); qv={t:idf.get(t,0.0) for t in qtok}
    def cos(a,b):
        dot=sum(a.get(t,0.0)*b.get(t,0.0) for t in set(a)|set(b))
        an=sum(v*v for v in a.values())**0.5; bn=sum(v*v for v in b.values())**0.5
        return dot/((an*bn)+1e-8)
    return np.array([cos(qv, d) for d in tfidf_docs], dtype=np.float32)
def hash_embed(text, dim=256):
    v=np.zeros(dim, dtype=np.float32)
    for tok in tokenize(text): v[hash(tok)%dim]+=1.0
    n=np.linalg.norm(v)+1e-8; return v/n
def vector_score(q, corpus):
    qv=hash_embed(q); mats=np.vstack([hash_embed(t) for t in corpus]); return mats@qv
def hybrid(q, alpha=0.6, k=3):
    tfidf_docs,idf=build_tfidf(corpus); kw=tfidf_score(q, tfidf_docs, idf); vs=vector_score(q, corpus)
    def norm(x): m,M=float(x.min()), float(x.max()); return (x-m)/((M-m)+1e-8) if M>m else np.zeros_like(x)
    h=alpha*norm(vs)+(1-alpha)*norm(kw); order=np.argsort(-h)[:k]
    return [(int(i), float(h[i]), float(kw[i]), float(vs[i]), corpus[i]) for i in order]
if __name__=="__main__":
    print("=== Day 14 — Hybrid Search ==="); alpha=0.6
    while True:
        q=input("\nQuery: ").strip()
        if q.lower() in ["exit","quit"]: break
        for rank,(i,h,kw,vs,t) in enumerate(hybrid(q, alpha=alpha, k=3),1):
            print(f"{rank}. H={h:.3f} | KW={kw:.3f} | VS={vs:.3f}  ->  {t}")
