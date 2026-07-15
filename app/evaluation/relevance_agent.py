import json

from app.evaluation.gemini_eval import generate_response
from app.evaluation.prompt_templates import build_prompt


# ============================================================
# Relevance Evaluation Agent
# ============================================================

def evaluate_relevance(question, ai_response, reference):
    """
    Evaluates how relevant the AI response is to the given question.
    """

    evaluation_task = """
Evaluate ONLY the relevance of the AI response to the given question.

Determine whether the response actually answers the user's question.

Scoring Rubric:

10 = Perfectly relevant. Directly answers the question.

8-9 = Mostly relevant. Answers the question with only minor unnecessary information.

6-7 = Generally relevant but partially addresses the question or includes noticeable irrelevant content.

4-5 = Somewhat relevant. Only part of the response relates to the question.

2-3 = Mostly irrelevant. Very little of the response answers the question.

1 = Almost completely irrelevant.

0 = Completely unrelated to the question.

Evaluation Rules:

• Evaluate ONLY relevance.
• Ignore factual correctness.
• Ignore grammar.
• Ignore completeness.
• Ignore hallucinations.
• Focus only on whether the response addresses the user's question.
• Use intermediate scores whenever appropriate.
• Give 10 only if the response is fully relevant.
• Give 0 only if the response is completely unrelated.

Return ONLY valid JSON in this format:

{
    "score": <0-10>,
    "reason": "<brief explanation>",
    "evidence": "<supporting evidence>",
    "status": "<PASS or FAIL>"
}
"""

    prompt = build_prompt(
        question=question,
        ai_response=ai_response,
        reference=reference,
        evaluation_task=evaluation_task
    )

    response = generate_response(prompt)

    try:
        result = json.loads(response)

    except Exception:

        result = {
            "score": None,
            "reason": "Unable to parse Gemini response.",
            "evidence": response,
            "status": "ERROR"
        }

    return result


# ============================================================
# Testing
# ============================================================

if __name__ == "__main__":

    print("=" * 60)
    print("Relevance Judge Agent")
    print("=" * 60)

    while True:

        question = input("\nQuestion: ")

        ai_response = input("\nAI Response: ")

        reference = input("\nReference Answer: ")

        result = evaluate_relevance(
            question,
            ai_response,
            reference
        )

        print("\n" + "=" * 60)
        print("Relevance Evaluation Result")
        print("=" * 60)

        print(json.dumps(result, indent=4))

        choice = input("\nEvaluate another response? (Y/N): ").strip().lower()

        if choice != "y":
            print("\nExiting Relevance Agent...")
            break