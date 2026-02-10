from analyzer import ask_ollama

def generate_question(resume_text, job_description, previous_questions):
    prompt = f"""
You are an interviewer.

Based on the resume and job description, generate a new interview question.

Do NOT repeat any of these questions:
{previous_questions}

Resume:
{resume_text}

Job Description:
{job_description}

Output only one new question.
"""
    return ask_ollama(prompt)


def evaluate_answer(question, answer):
    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Provide:

1. Technical accuracy (score out of 10)
2. Clarity (score out of 10)
3. Structure (score out of 10)
4. Confidence (score out of 10)
5. Overall feedback
6. Final score out of 10
"""
    return ask_ollama(prompt)
