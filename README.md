# Resume & Interview AI Agent

An AI-powered web application that analyzes resumes, compares them with job descriptions, and conducts mock interviews with feedback.

## Features
- Resume upload (PDF) and JD
- Resume analysis
- Skill gap detection
- Job match score
- Role-based interview questions
- Mock interview with answer evaluation

## Tech Stack
- Python
- Streamlit
- Ollama (Mistral model)
- pdfplumber

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Start Ollama:
   ollama run mistral

3. Run the app:
   streamlit run app.py
