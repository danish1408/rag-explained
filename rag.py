"""
What is RAG (Retrieval-Augmented Generation)?

An AI model only knows what it learned in training. Ask about YOUR documents
and it has to guess. RAG fixes this: before answering, it RETRIEVES the most
relevant documents, then GENERATES the answer using them -- an open-book exam
instead of a memory test.

This tiny demo shows the retrieval half with no downloads: given a question,
it finds the most relevant "document" by simple word overlap, then shows what
would be handed to the AI as context.

Real systems use embeddings + a vector store for retrieval (see my
embeddings and incremental_vector_search repos) -- the idea is identical.

Run:  python rag.py
Author: Danish Shabbir
"""

# a tiny "knowledge base" of private documents the model was never trained on
DOCS = {
    "leave_policy":  "Employees get 25 days of annual leave. Requests need manager approval.",
    "expenses":      "An expense claim must be submitted within 30 days with a receipt.",
    "wifi":          "The office wifi password is on the whiteboard in meeting room 2.",
    "security":      "Never share your password. Report phishing emails to IT immediately.",
}


def retrieve(question, docs, top=1):
    """Find the most relevant docs by simple word overlap (a stand-in for embeddings)."""
    q_words = set(question.lower().replace("?", "").split())
    scored = []
    for name, text in docs.items():
        tokens=text.lower().replace(".","").split()
        overlap = sum(1 for w in q_words if w in tokens) / (len(q_words) or 1)
        scored.append((overlap, name, text))
    scored.sort(reverse=True)
    return [(name, text) for score, name, text in scored[:top] if score > 0]


def answer(question, docs):
    hits = retrieve(question, docs)
    print(f"\nQ: {question}")
    if not hits:
        print("  (no relevant document found -- a plain model would have to guess)")
        return
    for name, text in hits:
        print(f"  retrieved -> [{name}]: {text}")
    print("  -> the AI now answers using THIS text, instead of guessing.")


if __name__ == "__main__":
    print("RAG = Retrieve, then Generate. First find the right page, THEN answer.")
    answer("How many days of annual leave do I get?", DOCS)
    answer("What's the wifi password?", DOCS)
    answer("When must I submit an expense claim?", DOCS)
