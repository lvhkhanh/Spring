---
name: mmlu-benchmark
description: '**WORKFLOW SKILL** — Create, run, validate, and analyze MMLU-style benchmark tests for language models. USE FOR: MMLU evaluation harnesses, multiple-choice prompt formats, subject-level scoring, few-shot and zero-shot evaluation, result analysis, reproducibility controls, benchmark reporting, and diagnosing model evaluation issues. DO NOT USE FOR: ordinary application unit tests, non-LLM QA, model training, benchmark claims without controlled methodology, or copyrighted dataset redistribution. INVOKES: file system tools for eval scripts and result files, terminal for benchmark execution, semantic search for existing eval patterns, web search for current benchmark documentation when needed.'
---

# MMLU Benchmark Test Skill

## Overview

This skill supports building and running MMLU-style evaluations for language models. It focuses on multiple-choice benchmark construction, prompt formatting, answer extraction, scoring, reproducibility, subject-level analysis, and honest reporting of limitations.

MMLU-style tests evaluate broad knowledge and reasoning across many academic and professional subjects. Treat benchmark results as comparative signals, not complete proof of model quality.

## Key Capabilities

### Evaluation Design
- Define zero-shot, few-shot, and chain-of-thought-free evaluation protocols
- Select subjects, splits, sample counts, and random seeds
- Keep train/dev/test data usage explicit
- Decide whether to run full benchmark, subject subset, smoke test, or regression comparison

### Prompt Construction
- Format multiple-choice questions with stable answer labels such as `A`, `B`, `C`, and `D`
- Use consistent system and user prompts across models
- Separate instructions, examples, question text, options, and answer format
- Avoid leaking correct answers, explanations, or metadata into the prompt

### Model Execution
- Run local or API-backed model inference with deterministic settings where possible
- Capture raw responses, normalized predictions, latency, token usage, and errors
- Support retries for transient failures without changing scored samples
- Keep provider, model version, temperature, max tokens, and date of run in metadata

### Scoring and Analysis
- Normalize model outputs to a single answer choice
- Compute overall accuracy, subject accuracy, category accuracy, and confidence intervals when needed
- Track invalid outputs, skipped samples, refusals, and parsing failures
- Compare runs against baselines with clear deltas and caveats

### Reproducibility and Integrity
- Version datasets, prompts, scripts, dependencies, and model identifiers
- Store immutable result artifacts for audit and comparison
- Prevent contamination from test answers in prompts, examples, logs, or fine-tuning data
- Report methodology details alongside headline scores

## Usage Examples

### Create an Evaluation Harness
```
Create a Python MMLU benchmark runner that loads JSONL questions,
formats multiple-choice prompts, calls a model client, extracts A-D answers,
and writes per-sample and aggregate results.
```

### Add Subject-Level Reporting
```
Extend the MMLU results script to report accuracy by subject,
macro average, micro average, invalid response rate, and sample count.
```

### Compare Two Models
```
Run the same MMLU subset against model_a and model_b with identical prompts,
temperature 0, fixed sample order, and a CSV comparison report.
```

### Debug Low Benchmark Score
```
Investigate why this MMLU run dropped from 72% to 48%.
Check prompt formatting, answer parsing, dataset split, model settings,
and invalid response handling.
```

## Common Patterns

### Prompt Template
```text
Answer the following multiple-choice question.
Respond with only one letter: A, B, C, or D.

Question:
{question}

Choices:
A. {choice_a}
B. {choice_b}
C. {choice_c}
D. {choice_d}

Answer:
```

### Few-Shot Prompt Template
```text
Answer each multiple-choice question with only one letter: A, B, C, or D.

Question:
{example_question_1}
Choices:
A. {example_a}
B. {example_b}
C. {example_c}
D. {example_d}
Answer: {example_answer}

Question:
{target_question}
Choices:
A. {target_a}
B. {target_b}
C. {target_c}
D. {target_d}
Answer:
```

### Result Record
```json
{
  "id": "abstract_algebra_0001",
  "subject": "abstract_algebra",
  "prompt_hash": "sha256:...",
  "gold": "C",
  "prediction": "C",
  "is_correct": true,
  "raw_response": "C",
  "model": "provider/model-name",
  "temperature": 0,
  "latency_ms": 842,
  "error": null
}
```

### Scoring Flow
```text
1. Load samples from the selected split
2. Build prompts using a versioned template
3. Run inference with fixed model settings
4. Extract a single answer choice from each response
5. Mark correct, incorrect, invalid, or errored
6. Aggregate by subject, category, and overall
7. Save raw and aggregate artifacts
```

### Minimal Answer Extraction
```python
import re

def extract_choice(text: str) -> str | None:
    cleaned = text.strip().upper()
    if cleaned in {"A", "B", "C", "D"}:
        return cleaned

    match = re.search(r"\b(?:ANSWER\s*[:\-]?\s*)?([ABCD])\b", cleaned)
    return match.group(1) if match else None
```

## Best Practices

### Methodology
- Define the benchmark protocol before running comparisons
- Use the same prompt, sample order, and inference settings for compared models
- Keep few-shot examples separate from scored test samples
- Report invalid output rate instead of silently dropping invalid samples
- Distinguish full MMLU from smaller smoke, dev, or subject-subset runs

### Prompting
- Ask for only the answer letter when scoring answer choice accuracy
- Avoid chain-of-thought requests unless the benchmark protocol explicitly requires them
- Keep formatting stable across subjects
- Use clear separators between examples and target questions

### Data Handling
- Do not redistribute benchmark datasets unless licensing permits it
- Store local dataset paths and checksums rather than copying large data into reports
- Avoid exposing gold answers in debug logs that may later be used as model context
- Keep test split data out of training, tuning, and prompt-example pools

### Reporting
- Include model name, provider, version, date, prompt template, split, sample count, and settings
- Report macro and micro averages when subject balance matters
- Include confidence intervals or bootstrap estimates for small samples
- Treat benchmark scores as one evaluation dimension alongside task-specific tests

## Troubleshooting

### Scores Are Unexpectedly Low
- Verify answer labels have not been shuffled without updating the gold label
- Check that the model is instructed to answer with `A`, `B`, `C`, or `D`
- Inspect invalid response rate and parsing failures
- Confirm the correct dataset split and subject mapping
- Compare a handful of raw prompts against expected formatting

### Scores Are Suspiciously High
- Check for gold answer leakage in prompts, examples, filenames, or metadata
- Ensure test samples were not used as few-shot examples
- Verify that cached responses belong to the current model and prompt hash
- Confirm the scorer is comparing predictions to the correct sample IDs

### Runs Are Not Reproducible
- Pin model identifiers, dependencies, prompt templates, and dataset versions
- Store random seeds and sample ordering
- Disable sampling or set temperature to `0` where supported
- Record provider-side model versions when available

### API or Runtime Failures
- Retry transient failures with backoff and preserve the final error state
- Separate model errors from invalid model answers
- Resume from saved per-sample results instead of rerunning completed samples
- Rate-limit requests to avoid provider throttling

## Integration Points

- **Evaluation frameworks**: lm-evaluation-harness, OpenAI Evals-style runners, custom Python scripts
- **Model providers**: local models, hosted APIs, inference gateways, batch APIs
- **Data formats**: CSV, JSONL, Parquet, Hugging Face datasets
- **Analysis tools**: pandas, notebooks, dashboards, markdown reports
- **CI workflows**: smoke evals, regression thresholds, nightly benchmark jobs
- **Governance**: reproducibility records, benchmark cards, contamination checks, audit artifacts
