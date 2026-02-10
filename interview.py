import os
from groq import Groq

def ask_groq(prompt):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def generate_question(resume_text, job_description, previous_questions):
    prompt = f"""
You are a technical interviewer.

Based on the resume and job description below, generate ONE unique interview question.
Do not repeat previous questions.

Resume:
{resume_text}

Job Description:
{job_description}

Previous Questions:
{previous_questions}

Generate only one new question.
"""
    return ask_groq(prompt)


def evaluate_answer(question, answer):
    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Provide:
1. Score out of 10
2. Strengths
3. Improvements
4. Final feedback
"""
    return ask_groq(prompt)
