import streamlit as st
import pandas as pd
import plotly.express as px
import tempfile

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skill_dictionary, extract_skills
from job_matcher import load_job_roles, match_resume_to_roles
from roadmap_generator import skill_gap_analysis, generate_roadmap
from report_generator import generate_report_pdf

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("AI Resume Analyzer & Job Recommendation System")

uploaded_file = st.file_uploader("Upload your resume", type=["pdf", "docx"])

if uploaded_file:
    raw_text = extract_resume_text(uploaded_file)
    cleaned = clean_text(raw_text)

    skill_df = load_skill_dictionary()
    found_skills = extract_skills(cleaned, skill_df)

    st.subheader("Skills Found")
    st.write([s["skill"] for s in found_skills])

    job_df = load_job_roles()
    results = match_resume_to_roles(cleaned, job_df)

    st.subheader("Recommended Roles (Top 3)")
    for r in results[:3]:
        st.write(f"{r['role']} — {r['score']}%")

    chart_df = pd.DataFrame(results)
    fig = px.bar(
        chart_df, x="role", y="score",
        title="Resume Match Score by Job Role",
        labels={"score": "Match Score (%)", "role": "Job Role"},
        color="score", color_continuous_scale="Blues"
    )
    st.plotly_chart(fig, use_container_width=True)

    target_role = st.selectbox("Select a target role", job_df["role"])
    required = job_df[job_df["role"] == target_role]["required_skills"].values[0]

    matched, missing = skill_gap_analysis(found_skills, required)
    st.subheader("Skill Gap")
    st.write("Matched:", list(matched))
    st.write("Missing:", list(missing))

    roadmap = generate_roadmap(list(missing))
    st.subheader("Suggested Learning Roadmap")
    for line in roadmap:
        st.write(line)

    score = next(r["score"] for r in results if r["role"] == target_role)

    # save chart to a temp file (works locally AND on Streamlit Cloud)
    chart_tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    chart_image_path = chart_tmp.name
    chart_tmp.close()
    fig.write_image(chart_image_path, width=800, height=450)

    pdf_bytes = generate_report_pdf(
        target_role, score,
        [s["skill"] for s in found_skills],
        matched, missing, roadmap,
        chart_image_path
    )

    st.download_button(
        label="Download Analysis Report (PDF)",
        data=pdf_bytes,
        file_name="resume_analysis_report.pdf",
        mime="application/pdf"
    )
else:
    st.info("Upload a PDF or DOCX resume to get started.")