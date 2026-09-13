# What is RAG?

**Retrieval-Augmented Generation — how AI answers questions about YOUR documents.**

An AI model only knows what it learned during training. Ask it about your internal
docs and it has to guess — and guessing is where hallucinations come from. RAG fixes
this: before answering, it **retrieves** the relevant documents, then **generates**
the answer using them. An open-book exam instead of a memory test.

> 🎥 Companion code to my 60-second explainer video.

## Run it
```bash
python rag.py
```
Given a question, it finds the most relevant "document" and shows what would be handed
to the AI as context — so the model answers from real text instead of guessing.

## The real version
Production RAG uses **embeddings** + a **vector store** for retrieval. See my related
repos:
- [embeddings_explained](https://github.com/danish1408/embeddings_explained)
- [incremental_vector_search](https://github.com/danish1408/incremental_vector_search)

The idea is identical — this demo just uses simple word matching so you can read
exactly what's happening.

---
*One AI concept at a time.* **Danish Shabbir** — Test Automation → AI / ML
