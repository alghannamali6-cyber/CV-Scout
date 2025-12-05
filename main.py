import streamlit as st
import os
import re
from jd_Agent import JDAgent
from cv_agent import CVAgent
from comp_agent import ComparisonAgent
from config import CV_FOLDER, MAX_CVS_UPLOAD

st.set_page_config(page_title="AI-Powered Candidate Evaluation", layout="wide")
st.title("AI-Powered Candidate Evaluation")

# Step 1: JD
st.header("1️⃣ Paste Job Description")
jd_text = st.text_area("Paste your Job Description here", height=200)

# Step 2: Upload CVs
st.header("2️⃣ Upload Candidate CVs")
cv_files = st.file_uploader(
    f"Upload up to {MAX_CVS_UPLOAD} CV PDFs",
    type=["pdf"],
    accept_multiple_files=True,
    key="cv_upload"
)

os.makedirs(CV_FOLDER, exist_ok=True)

# Helper: Extract overall score
def extract_overall_score(text):
    match = re.search(r"Overall Score:\s*(\d+)", text)
    if match:
        return int(match.group(1))
    return 0

# Step 3: Process & Compare
if st.button("✅ Process & Rank Candidates") and jd_text and cv_files:
    if len(cv_files) > MAX_CVS_UPLOAD:
        st.warning(f"You can only upload up to {MAX_CVS_UPLOAD} CVs.")
    else:
        jd_agent = JDAgent()
        jd_chunks = jd_agent.process_from_text(jd_text)

        results = []
        st.info("Processing CVs and comparing with JD...")
        progress_bar = st.progress(0)
        total_cvs = len(cv_files)

        for i, cv_file in enumerate(cv_files):
            cv_path = os.path.join(CV_FOLDER, cv_file.name)
            with open(cv_path, "wb") as f:
                f.write(cv_file.getbuffer())

            st.write(f"Processing CV {i+1}/{total_cvs}: {cv_file.name}")

            cv_agent = CVAgent(cv_path)
            cv_chunks = cv_agent.process()

            comparator = ComparisonAgent(jd_chunks, cv_chunks)
            try:
                result_text = comparator.compare()
            except Exception as e:
                result_text = f"Error processing CV: {e}"

            score = extract_overall_score(result_text)

            results.append({
                "candidate": cv_file.name,
                "score": score,
                "output": result_text
            })

            progress_bar.progress((i + 1) / total_cvs)

        # Rank by overall score
        results_sorted = sorted(results, key=lambda x: x["score"], reverse=True)

        st.header("3️⃣ Ranked Candidates")
        for idx, candidate in enumerate(results_sorted, start=1):
            st.subheader(f"{idx}. {candidate['candidate']} — Score: {candidate['score']}")
            with st.expander("Show Section Details"):
                explanation_lines = candidate["output"].split("\n")
                for line in explanation_lines:
                    # Highlight overall score
                    if line.strip().startswith("Overall Score"):
                        st.markdown(f"**{line.strip()}**")
                    # Sub-bullets with ticks/crosses
                    elif line.strip().startswith("✅") or line.strip().startswith("❌"):
                        st.text(line.strip())
                    # Section header line with numeric score
                    else:
                        st.text(line.strip())

        st.success("✅ All candidates processed!")
