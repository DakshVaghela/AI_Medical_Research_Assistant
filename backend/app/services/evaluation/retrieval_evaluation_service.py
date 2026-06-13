import json

from app.services.retrieval.retrieval_service import (
    retrieve_context
)


def evaluate_retrieval():

    with open(
        "evaluation/retrieval_test_set.json",
        "r"
    ) as f:

        tests = json.load(f)

    total_hit = 0
    total_recall = 0
    total_precision = 0
    total_mrr = 0

    results = []

    for test in tests:

        retrieved = retrieve_context(
            test["question"]
        )

        retrieved_ids = [
            chunk["chunk_id"]
            for chunk in retrieved
        ]

        expected_ids = set(
            test["expected_chunks"]
        )

        retrieved_set = set(
            retrieved_ids
        )

        correct = (
            expected_ids
            &
            retrieved_set
        )

        precision = (
            len(correct)
            /
            len(retrieved_ids)
            if retrieved_ids
            else 0
        )
        mrr = 0

        for idx, chunk_id in enumerate(
            retrieved_ids,
            start=1
        ):

            if chunk_id in expected_ids:

                mrr = 1 / idx
                break

        hit = (
                1
                if len(correct) > 0
                else 0
            )

        recall = (
            len(correct)
            /
            len(expected_ids)
        )

        total_hit += hit
        total_recall += recall
        total_precision += precision
        total_mrr += mrr

        results.append({
            "question": test["question"],
            "retrieved": retrieved_ids,
            "expected": list(expected_ids),
            "hit": hit,
            "recall": round(recall, 2),
            "precision": round(precision, 2),
            "mrr": round(mrr, 2)
        })

    total = len(tests)
    mrr = 0

    return {
        "hit_rate":
            round(
                total_hit / total,
                2
            ),

        "avg_recall":
            round(
                total_recall / total,
                2
            ),

        "avg_precision":
            round(
                total_precision / total,
                2
            ),

        "mrr":
            round(
                total_mrr / total,
                2
            ),

        "results":
            results
    }