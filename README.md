# RAG Tutorial 13 — RAG Evaluation Framework

<p align="center">
  <a href="https://github.com/BellaBe/mastering-rag"><img src="https://img.shields.io/badge/Series-Mastering_RAG-blue?style=for-the-badge" /></a>
  <img src="https://img.shields.io/badge/Part-13_of_16-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Difficulty-Advanced-orange?style=for-the-badge" />
</p>

> **Part of the [Mastering RAG](https://github.com/BellaBe/mastering-rag) tutorial series**  
> Previous: [12 — Graph RAG](https://github.com/BellaBe/rag-12-graph-rag) | Next: [14 — Real-Time Streaming](https://github.com/BellaBe/rag-14-realtime-streaming)

---

## Real-World Scenario

> Your RAG chatbot is live. Users are complaining: "It gives wrong answers sometimes." But which answers are wrong? And why? Is the retrieval bad (wrong chunks), the generation bad (LLM ignores context), or both? You need **automated metrics** — not manual review of 1,000 conversations. This framework gives you three scores per query (faithfulness, relevance, precision) so you can pinpoint failures and prioritize fixes.

---

## What You'll Build

An evaluation framework that measures RAG output quality using **RAGAS-style metrics**: faithfulness, answer relevance, and context precision — powered by LLM-as-judge. Upload evaluation datasets, run scoring, and view per-sample and aggregate results.

```
Input: { query, context_chunks[], answer }
  ↓
Evaluate:
  Faithfulness:      0.92  (is the answer grounded in context?)
  Answer Relevance:  0.88  (does the answer address the query?)
  Context Precision:  0.75  (are the retrieved chunks useful?)
  ↓
Action: Context precision is low → improve retrieval
```

## Key Concepts

- **Faithfulness**: does the answer only use information from the retrieved context?
- **Answer relevance**: does the answer actually address the user's question?
- **Context precision**: are the retrieved chunks relevant to the query?
- **LLM-as-judge**: use an LLM to evaluate RAG outputs at scale
- **Per-sample vs. aggregate**: drill into individual failures or track system-level trends

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.11+ · FastAPI · OpenAI (LLM-as-judge) |
| Frontend | React 19 · Vite · Tailwind CSS · Recharts |

## Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # OPENAI_API_KEY for LLM-as-judge
uvicorn app.main:app --reload --port 8007
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 — paste/upload evaluation dataset, select metrics, view scores.

## Dataset Format

Each evaluation sample:

```json
{
  "query": "What is the capital of France?",
  "context": ["France is a country in Europe. Its capital is Paris."],
  "answer": "The capital of France is Paris."
}
```

## What You'll Learn

1. Why you can't improve RAG without measuring it first
2. The three core RAGAS metrics and what they reveal
3. How to use an LLM to evaluate another LLM's outputs
4. How to build and curate evaluation datasets
5. How to interpret scores and decide what to optimize next

## Prerequisites

- Python 3.11+ and Node.js 18+
- A working RAG system to evaluate (any from Tutorials 05–12)
- OpenAI API key (for LLM-as-judge)

## Exercises

1. **Build an eval dataset**: From your Tutorial 05 RAG pipeline, collect 20 query-context-answer triples. Run them through the evaluator. What's your baseline score?
2. **Improve and re-measure**: Take the lowest-scoring samples, improve the retrieval or prompt, and re-evaluate. Track the improvement.
3. **Judge agreement**: Run the same samples through the evaluator 3 times. How consistent are the scores? (This measures LLM-as-judge reliability.)
4. **Human vs. LLM evaluation**: Manually score 10 samples yourself, then compare with the automated scores. Where do they disagree?
5. **Cross-tutorial comparison**: Evaluate the same queries on Tutorial 05 (basic RAG) vs. Tutorial 09 (with re-ranking). Quantify the improvement.

## Common Mistakes

| Mistake | Why It Happens | How to Fix |
|---------|---------------|------------|
| High faithfulness but low answer relevance | LLM sticks to context but doesn't actually answer the question | Improve the RAG prompt to emphasize addressing the query directly |
| Low context precision but high answer relevance | LLM gets lucky despite bad retrieval | Improve retrieval (chunking, reranking); don't rely on the LLM to compensate |
| Evaluator scores vary wildly between runs | LLM-as-judge is non-deterministic | Set temperature=0 for the evaluator; average over 3 runs |
| 100% faithfulness on every sample | Evaluation prompt is too lenient | Make the faithfulness prompt stricter: "Check if EVERY claim in the answer has a supporting sentence in the context" |

## Further Reading

- [RAGAS: Automated Evaluation of Retrieval Augmented Generation](https://arxiv.org/abs/2309.15217) — The RAGAS paper (Es et al., 2023)
- [RAGAS Documentation](https://docs.ragas.io/) — Official framework documentation
- [Galileo RAG Evaluation](https://www.rungalileo.io/blog/mastering-rag-how-to-evaluate-retrieval-augmented-generation-pipelines) — Practical evaluation guide
- [LLM-as-Judge: Best Practices](https://arxiv.org/abs/2306.05685) — Research on using LLMs for evaluation (Zheng et al., 2023)
- [DeepEval](https://docs.confident-ai.com/) — Another RAG evaluation framework for comparison

## Next Steps

Now that you can measure quality, head to **[Tutorial 14 — Real-Time RAG with Streaming](https://github.com/BellaBe/rag-14-realtime-streaming)** to build production-ready delivery patterns.

---

<p align="center">
  <sub>Part of <a href="https://github.com/BellaBe/mastering-rag">Mastering RAG — From Zero to Production</a></sub>
</p>
