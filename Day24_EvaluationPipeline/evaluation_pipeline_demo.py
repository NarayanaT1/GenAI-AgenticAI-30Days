# Day 24 – AI Evaluation Pipeline Demo

test_cases = [
    {
        "prompt": "What is AI?",
        "expected_keywords": ["intelligence", "machines"],
        "model_output": "Artificial intelligence enables machines to simulate human intelligence."
    },
    {
        "prompt": "What is RAG?",
        "expected_keywords": ["retrieval", "generation"],
        "model_output": "RAG combines retrieval with generation to improve factual accuracy."
    },
    {
        "prompt": "What is prompt injection?",
        "expected_keywords": ["attack", "instructions"],
        "model_output": "Prompt injection is an attack that manipulates model instructions."
    }
]

def evaluate_output(output, expected_keywords):
    output_lower = output.lower()
    matched = sum(1 for kw in expected_keywords if kw.lower() in output_lower)
    score = matched / len(expected_keywords)
    passed = score >= 0.5
    return score, passed

def run_pipeline():
    results = []
    for case in test_cases:
        score, passed = evaluate_output(case["model_output"], case["expected_keywords"])
        results.append({
            "prompt": case["prompt"],
            "score": score,
            "passed": passed,
            "output": case["model_output"]
        })
    return results

if __name__ == "__main__":
    print("=== Day 24 – AI Evaluation Pipeline ===")
    results = run_pipeline()
    for r in results:
        print(f"Prompt: {r['prompt']}")
        print(f"Output: {r['output']}")
        print(f"Score: {r['score']:.2f}")
        print("Status:", "PASS" if r["passed"] else "FAIL")
        print("-" * 40)
