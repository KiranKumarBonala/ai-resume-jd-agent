import streamlit as st
from src.search import search

st.set_page_config(page_title="Resume–JD Matcher", layout="wide")

st.title("🤖 AI Resume Matcher")
st.write("Paste a Job Description to find the best matching resumes.")

jd = st.text_area("Job Description", height=250)

if st.button("Find Matches"):
    if jd.strip():
        results = search(jd, top_k=3)

        for i, res in enumerate(results, 1):
            st.subheader(f"Candidate {i}")
            st.write(res[:1200])
    else:
        st.warning("Please paste a Job Description.")
