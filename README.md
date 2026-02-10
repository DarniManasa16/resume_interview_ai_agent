# Resume & Interview AI Agent

An AI-powered web application that analyzes resumes, detects skill gaps, and conducts mock interviews with feedback.

## Live Demo
https://resume-interview-ai-agent.streamlit.app/

## Features
- Upload resume (PDF)
- Resume analysis
- Skill gap detection
- Job match score
- Role-based interview questions
- 5-question mock interview
- AI-based answer evaluation

## Tech Stack
- Python
- Streamlit
- Groq API (LLaMA 3)
- pdfplumber

## Project Structure
resume_ai_agent/
│
├── app.py
├── resume_parser.py
├── analyzer.py
├── interview.py
├── requirements.txt
└── README.md

## How to Run Locally

1. Clone the repo:
   git clone <your-repo-link>

2. Go into the folder:
   cd resume_ai_agent

3. Install dependencies:
   pip install -r requirements.txt

4. Create a `.env` file:
   GROQ_API_KEY=your_api_key_here

5. Run the app:
   streamlit run app.py
