# Approach Document — SHL AI Assessment Recommender

## 1. Design Choices

The system was designed as a conversational recommendation API that suggests SHL assessments based on hiring requirements. The main goals were:

- Support vague queries through clarification
- Preserve constraints across multiple turns
- Recommend only SHL catalog items
- Support refinement (e.g., adding personality requirements later)
- Compare assessments on request
- Prevent out-of-scope or unsafe responses

The architecture follows:

User Query

↓

Guardrails

↓

Constraint Extraction (LLM)

↓

Semantic Retrieval (FAISS)

↓

Recommendation Logic

↓

Response Formatting

↓

Evaluation


FastAPI was used for serving the API and Swagger UI for testing.

---

## 2. Retrieval Setup

Retrieval uses:

- Sentence embeddings for semantic search
- FAISS vector index for nearest-neighbor retrieval
- Category-based reranking
- Deduplication of retrieved assessments

The SHL catalog is embedded into vectors and stored in a FAISS index.

Queries retrieve relevant assessments using constraints such as:

- skills
- seniority
- personality
- communication
- leadership

Combined constraints are supported.

Example:

Need Java developer

↓

Add personality tests

↓

Java + personality recommendations

Retrieval quality was measured using Recall@10.

Results:

Mean Recall@10 = 0.94

across 8 conversation traces.

---

## 3. Prompt Design

LLM prompts were used for:

### Constraint extraction

Extract:

- skills
- seniority
- personality requirements
- communication requirements
- leadership requirements

Constraints remain cumulative across turns.

Example:

Need senior Java developer

↓

Actually make it entry level

↓

Updated constraints returned


### Comparison

Supports:

Compare Java 8 and OPQ

↓

Structured comparison response


Guardrails reject:

- prompt injection
- legal advice
- medical advice
- non-SHL recommendations

---

## 4. Evaluation Approach

Evaluation included:

### Hard Evaluations

Schema compliance:

PASS

Catalog-only recommendations:

PASS

Turn cap (<8):

PASS


### Retrieval Metric

Mean Recall@10:

0.94


### Behavior Probes

Measured:

- clarification behavior
- refinement handling
- prompt injection refusal
- legal refusal
- comparison handling
- hallucination prevention

Behavior Probe Pass Rate:

100%

---

## 5. What Did Not Work Initially

Several issues appeared during development:

### Leadership retrieval mismatch

Leadership constraints were initially not retrieved correctly due to mismatch between retrieval queries and catalog terminology.

Improvement:

Adjusted retrieval queries and recommender logic.

Result:

Leadership Recall improved from:

0.0

↓

1.0


### Deployment memory limits

Initial deployment exceeded Render free-tier memory due to embedding dependencies.

Improvement:

- Reduced dependency size
- Optimized embedding setup
- Simplified deployment requirements

Result:

Successful deployment while preserving retrieval performance.

---

## 6. AI Tool Usage

AI tools were used for:

- debugging
- deployment troubleshooting
- evaluation design
- documentation refinement
- code improvement suggestions

Architecture choices, testing, and validation were performed manually.

---

## Public Deployment

API:

https://shl-ai-assessment-recommender-08nr.onrender.com

Swagger:

https://shl-ai-assessment-recommender-08nr.onrender.com/docs

Health:

https://shl-ai-assessment-recommender-08nr.onrender.com/health