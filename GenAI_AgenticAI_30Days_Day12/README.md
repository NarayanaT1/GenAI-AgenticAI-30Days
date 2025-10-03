# Day 12 – Retrieval-Augmented Generation (RAG) with PDFs

This demo shows how to implement a **toy RAG pipeline** using a sample PDF.

## Steps
1. Load a PDF (`sample.pdf` provided here)
2. Split the text into chunks
3. Convert chunks into toy embeddings (hash-based vectors)
4. Store in a simple in-memory index
5. Search with a query → retrieve relevant chunks

## Run the demo
```bash
cd day12_rag_with_pdfs
python rag_with_pdfs.py
```

## Example Query
```
Query: What is AI about?
Top results:
- Artificial Intelligence (AI) is a broad field of computer science. Key areas include...
```

## Notes
- This is a **safe, toy demo** (no external API calls).
- Embeddings are **hash-based** for educational purposes.
- Independent personal project © 2025 Srimannarayana Reddi Tadi • CloudByteHub.ai | MIT License
