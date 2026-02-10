import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()["response"]


def analyze_resume(resume_text, job_description):
    prompt = f"""
You are an AI career coach.

Analyze the resume against the job description.

Resume:
{resume_text}

Job Description:
{job_description}

Provide:

1. Resume strengths
2. Resume weaknesses
3. Skill gap analysis
4. Match score (0–100%)
5. 5 role-based interview questions
"""
    return ask_ollama(prompt)
