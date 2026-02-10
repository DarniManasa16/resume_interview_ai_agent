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


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an AI resume analyzer.

Compare the following resume with the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:
1. Match score out of 100
2. Missing skills
3. Improvement suggestions
"""

    return ask_groq(prompt)
