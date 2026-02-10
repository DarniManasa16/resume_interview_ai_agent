import streamlit as st
from resume_parser import extract_resume_text
from analyzer import analyze_resume
from interview import generate_question, evaluate_answer

# Page settings
st.set_page_config(
    page_title="Resume & Interview AI Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Resume & Interview AI Agent")
st.markdown("### Your personal AI career coach")
st.divider()

# ---------------- LAYOUT: TWO COLUMNS ----------------
col1, col2 = st.columns(2)

resume_text = ""
job_description = ""

with col1:
    st.header("📄 Upload Resume")
    uploaded_file = st.file_uploader("Upload PDF Resume", type=["pdf"])

    if uploaded_file is not None:
        resume_text = extract_resume_text(uploaded_file)
        st.text_area("Resume Content", resume_text, height=250)

with col2:
    st.header("💼 Job Description")
    job_description = st.text_area(
        "Paste job description here",
        height=250
    )

# ---------------- RESUME ANALYSIS ----------------
st.divider()
st.subheader("📊 Resume Analysis")

if st.button("Analyze Resume", use_container_width=True):
    if resume_text and job_description:
        with st.spinner("Analyzing with AI..."):
            result = analyze_resume(resume_text, job_description)
        st.success("Analysis Complete")
        st.write(result)
    else:
        st.warning("Please upload a resume and paste a job description.")

# ---------------- INTERVIEW SECTION ----------------
st.divider()
st.header("🎤 Mock Interview")

# Initialize session memory
if "previous_questions" not in st.session_state:
    st.session_state["previous_questions"] = []

if "question_count" not in st.session_state:
    st.session_state["question_count"] = 0

# Progress bar
progress = st.session_state["question_count"] / 5
st.progress(progress, text=f"Interview progress: {st.session_state['question_count']}/5 questions")

# Generate question
if st.button("Generate Interview Question", use_container_width=True):
    if resume_text and job_description:
        if st.session_state["question_count"] < 5:
            question = generate_question(
                resume_text,
                job_description,
                st.session_state["previous_questions"]
            )
            st.session_state["question"] = question
            st.session_state["previous_questions"].append(question)
            st.session_state["question_count"] += 1
        else:
            st.success("Interview completed! You have answered 5 questions.")
    else:
        st.warning("Upload resume and paste job description first.")

# Display question
if "question" in st.session_state:
    st.subheader("Interview Question")
    st.info(st.session_state["question"])

    user_answer = st.text_area("Your Answer", height=150)

    if st.button("Evaluate Answer", use_container_width=True):
        if user_answer:
            with st.spinner("Evaluating answer..."):
                feedback = evaluate_answer(
                    st.session_state["question"],
                    user_answer
                )
            st.subheader("Interview Feedback")
            st.success("Evaluation Complete")
            st.write(feedback)
        else:
            st.warning("Please enter your answer.")
