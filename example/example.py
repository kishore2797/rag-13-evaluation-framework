#!/usr/bin/env python3
"""
RAG Tutorial 13 — RAG Evaluation Framework
Minimal example: score a single RAG output with simple faithfulness and relevance heuristics.
Run: python example.py (no extra deps)
"""
def faithfulness_score(answer: str, context: str) -> float:
    """Heuristic: share of answer words that appear in context (proxy for grounding)."""
    a_words = set(w.lower() for w in answer.split() if len(w) > 2)
    c_lower = context.lower()
    if not a_words:
        return 1.0
    in_context = sum(1 for w in a_words if w in c_lower)
    return in_context / len(a_words)


def relevance_score(query: str, answer: str) -> float:
    """Heuristic: share of query words that appear in answer (proxy for addressing the question)."""
    q_words = set(w.lower() for w in query.split() if len(w) > 2)
    a_lower = answer.lower()
    if not q_words:
        return 1.0
    in_answer = sum(1 for w in q_words if w in a_lower)
    return in_answer / len(q_words)


def main():
    query = "What is RAG?"
    context = "RAG stands for retrieval-augmented generation. It combines retrieval and generation."
    answer = "RAG is retrieval-augmented generation that combines retrieval with generation."
    f = faithfulness_score(answer, context)
    r = relevance_score(query, answer)
    print("Query:", query)
    print("Context:", context)
    print("Answer:", answer)
    print("Faithfulness (words from context):", round(f, 2))
    print("Relevance (query words in answer):", round(r, 2))
    print("\n→ Production uses LLM-as-judge (e.g. RAGAS) for faithfulness and answer relevance.")


if __name__ == "__main__":
    main()
