# SHL AI Assessment Recommender

An AI-powered conversational recommendation system that suggests relevant SHL assessments based on hiring requirements.

The system supports:

- Multi-turn conversations
- Constraint refinement
- Personality/communication requirements
- Assessment comparison
- Prompt injection resistance
- Guardrails for out-of-scope requests
- Retrieval-Augmented Generation (FAISS + semantic search)

---

## Live Demo

API Docs:

https://shl-ai-assessment-recommender-08nr.onrender.com/docs

Health Endpoint:

https://shl-ai-assessment-recommender-08nr.onrender.com/health

---

## Features

### Clarification

Input:

Need an assessment

Output:

What role, skill, or position are you hiring for?

---

### Recommendations

Input:

Need entry level Java developer

Output:

Relevant SHL Java assessments

---

### Refinement

Input:

Need Java developer

Add personality tests

Output:

Java + personality assessments

---

### Comparison

Input:

Compare Java 8 and OPQ

Output:

Structured comparison

---

### Guardrails

Rejects:

- Prompt injection
- Legal advice
- Medical advice
- Non-SHL recommendations

---

## Architecture

User Query
↓
Constraint Extraction (LLM)
↓
Guardrails
↓
FAISS Retrieval
↓
Recommendation Agent
↓
Response Generation

---

## Tech Stack

- FastAPI
- FAISS
- SentenceTransformers
- Groq API
- Render Deployment

---

## Evaluation

Tested for:

✓ Clarification

✓ Refinement

✓ Personality update

✓ Communication

✓ Leadership

✓ Comparison

✓ Prompt injection

✓ Legal/medical refusal

---

## Deployment

Public API:

https://shl-ai-assessment-recommender-08nr.onrender.com

Swagger:

https://shl-ai-assessment-recommender-08nr.onrender.com/docs

---

## Run Locally

Install:

pip install -r requirements.txt

Run:

uvicorn app.main:app --reload

Open:

localhost:8000/docs