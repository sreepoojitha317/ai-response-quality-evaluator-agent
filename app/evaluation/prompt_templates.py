# ============================================================
# Common Prompt Template Builder
# ============================================================

def build_prompt(question, ai_response, reference, evaluation_task):
    """
    Builds a standardized evaluation prompt for all Judge Agents.
    """

    prompt = f"""
You are an AI Evaluation Expert.

Your job is to evaluate an AI-generated response.

Question:
{question}

AI Response:
{ai_response}

Reference Answer / Retrieved Context:
{reference}

Evaluation Task:
{evaluation_task}

Instructions:
- Evaluate ONLY the requested criterion.
- Give a score between 0 and 10.
- Explain your reasoning clearly.
- Cite evidence from the reference whenever possible.
- Do not evaluate anything outside the requested criterion.

Return your response ONLY in the following JSON format:

{{
    "score": <number>,
    "reason": "<short explanation>",
    "evidence": "<supporting evidence>",
    "status": "<PASS or FAIL>"
}}

Do not return markdown.
Do not return extra text.
Return only valid JSON.
"""

    return prompt