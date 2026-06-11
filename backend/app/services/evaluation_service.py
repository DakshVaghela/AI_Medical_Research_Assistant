import json

from app.services.document_chat_service import (
    chat_with_document
)


def evaluate_document_rag():

    with open(
        "evaluation/diabetes_test_set.json",
        "r"
    ) as f:

        test_cases = json.load(f)

    results = []

    total = len(test_cases)
    passed = 0

    for test in test_cases:

        response = chat_with_document(
            query=test["question"]
        )

        answer = response["answer"]

        score = 1

        for keyword in test[
            "expected_answer"
        ]:

            if keyword.lower() not in answer.lower():

                score = 0

        if score == 1:
            passed += 1

        results.append({
            "question":
                test["question"],
            "score":
                score,
            "answer":
                answer
        })

    return {
        "total_questions":
            total,
        "passed":
            passed,
        "accuracy":
            round(
                passed / total * 100,
                2
            ),
        "results":
            results
    }