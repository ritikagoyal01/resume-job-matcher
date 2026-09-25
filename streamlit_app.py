import streamlit as st
from pypdf import PdfReader

from skill_extractor import extract_skills
from text_similarity import calculate_similarity

# page configuration

st.set_page_config(
    page_title="Resume Job Matcher",
    page_icon="🤖",
    layout="wide"
)

# pdf text extraction
def extract_text_from_pdf(uploaded_file):

    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text+"/n"

    return text

# skill match

def calculate_match(resume_skills,job_skills):

    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

        else:
            missing_skills.append(skill)

    job_skill_count = len(job_skills)

    if job_skill_count > 0:
        skill_score = (
            len(matched_skills)/
            len(job_skills)
        )*100

    else:
        skill_score = 0

    return matched_skills,missing_skills,skill_score

# title
st.title("🤖 Resume Job Matcher")

st.write(
    "Upload your resume and paste a job description"
    "to see how well your resume matches the job"
)

# resume upload
uploaded_resume = st.file_uploader(
    "Upload your resume",
    type=["pdf"]
)

# job description
job_description = st.text_area(
    "Paste Job Description",
    height = 250,
    placeholder="Paste the job description here...."
)

# analyze button
if st.button("Analyze Resume"):
    if uploaded_resume is None:
        st.warning("Please upload your resume PDF.")

    elif not job_description.strip():
        st.warning("Please paste a job description.")

    else:
        # extract resume text
        resume_text = extract_text_from_pdf(uploaded_resume)

        # extract skills
        resume_skills = extract_skills(resume_text)
        job_skills = extract_skills(job_description)

        # calculate skill matching
        matched_skills,missing_skills,skill_score = (
            calculate_match(
                resume_skills,
                job_skills
            )
        )

        # calculate tf-idf score
        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # final score
        final_score = (
            (skill_score*0.7)
            +
            (similarity_score*0.3)
        )

        # show results
        st.divider()

        st.subheader("Match Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Final Match Score",
                f"{final_score:.1f}%"
            )

    with col3:

        st.metric(
            "Text Similarity",
            f"{similarity_score:.1f}%"
        )

    # matched skills
    st.subheader("Matched Skills")

    if matched_skills:
        for skill in matched_skills:
            st.success(skill)
    else:
        st.info("No matching skills found.")

    # missing skills
    st.subheader("Missing Skills")
    if missing_skills:
        for skill in missing_skills:
            st.error(skill)
    else:
        st.success("No missing skills found.")