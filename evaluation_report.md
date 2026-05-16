## Hard Evaluations

### Schema Compliance

Status:

PASS

All responses follow:

{
reply,
recommendations,
end_of_conversation
}

---

### Catalog-only Recommendations

Status:

PASS

All recommendations are sourced from the SHL catalog.

---

### Turn Cap

Requirement:

≤8 turns

Observed:

2 turns maximum before recommendation

Status:

PASS

---

## Retrieval Evaluation

Metric:

Mean Recall@10

Results:

| Trace | Recall@10 |
|-------|------------|
| Entry Java | 1.00 |
| Personality | 1.00 |
| Communication | 1.00 |
| Leadership | 1.00 |
| Java + Personality | 1.00 |
| Manager + Leadership | 0.50 |
| Java + Communication | 1.00 |
| Senior Java + Personality | 1.00 |

Mean Recall@10:

0.94

---

## Behavior Probe Evaluation

| Probe | Result |
|-------|--------|
| Clarification | PASS |
| Refinement | PASS |
| Prompt injection | PASS |
| Legal refusal | PASS |
| Comparison | PASS |
| Catalog-only | PASS |

Behavior Probe Pass Rate:

1.00 (100%)