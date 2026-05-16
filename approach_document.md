# Approach Document — SHL AI Assessment Recommender

## 1. Problem Understanding

The objective was to build a conversational recommendation system capable of suggesting relevant SHL assessments based on hiring requirements while supporting clarification, refinement, comparison, and safe responses.

The system must:

- Recommend only SHL assessments
- Handle multi-turn conversations
- Refine constraints over time
- Support assessment comparison
- Resist prompt injection and out-of-scope queries

---

## 2. System Architecture

Pipeline:

User Query

↓

Guardrails

↓

Constraint Extraction (LLM)

↓

FAISS Retrieval

↓

Recommendation Generation

↓

Response Formatting

The API is implemented using FastAPI and deployed publicly.

---

## 3. Constraint Extraction

An LLM extracts:

- Skills
- Seniority
- Personality requirements
- Communication requirements
- Leadership requirements
- Duration constraints

Constraints are cumulative across turns.

Example:

User:

Need Java developer

User:

Add personality tests

Result:

Java + personality retained

---

## 4. Retrieval Strategy

The system uses:

- Sentence embeddings
- FAISS similarity search
- Semantic retrieval
- Category-based reranking
- Deduplication

Retrieved assessments are restricted to the SHL catalog.

---

## 5. Conversation Handling

Supports:

### Clarification

Incomplete requests trigger follow-up questions.

Example:

"I need an assessment"

↓

"What role, skill, or position are you hiring for?"

---

### Refinement

User updates modify existing constraints.

Example:

Senior Java developer

↓

Actually make it entry level

↓

Updated recommendations returned

---

### Comparison

Supports:

Compare Java 8 and OPQ

↓

Structured assessment comparison

---

## 6. Guardrails

Rejects:

- Prompt injection
- Legal advice
- Medical advice
- Non-SHL recommendations

This ensures safe and domain-specific responses.

---

## 7. Evaluation

Evaluation included:

✓ Clarification

✓ Refinement

✓ Comparison

✓ Guardrails

✓ Multi-turn updates

✓ Health endpoint

All tests passed.

---

## 8. Deployment Challenges

Initial deployment exceeded Render memory limits due to embedding model dependencies.

Optimization steps:

- Reduced embedding model size
- Optimized dependencies
- Switched to CPU-compatible deployment setup

Result:

Successful public deployment while preserving retrieval quality.

---

## 9. AI Usage Disclosure

AI tools were used for:

- Debugging
- Deployment troubleshooting
- Code refinement
- Documentation assistance

Architecture decisions, testing, and validation were performed manually.

---

## Public Deployment

API:

https://shl-ai-assessment-recommender-08nr.onrender.com

Swagger:

https://shl-ai-assessment-recommender-08nr.onrender.com/docs

Health:

https://shl-ai-assessment-recommender-08nr.onrender.com/health