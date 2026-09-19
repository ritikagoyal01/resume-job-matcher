from skill_extractor import extract_skills
from text_similarity import calculate_similarity
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text +"\n"

    return text

def calculate_match(resume_skills, job_skills):
    matched_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) > 0:
        match_score = (len(matched_skills) / len(job_skills)) * 100
    else:
        match_score = 0

    return matched_skills, missing_skills, match_score


if __name__ == "__main__":

    """
    resume_skills = [
        "Python",
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Scikit-learn",
        "OpenCV",
        "Git",
        "GitHub"
    ]

    job_skills = [
        "Python",
        "SQL",
        "FastAPI",
        "Git",
        "Docker",
        "PostgreSQL"
    ]

    matched, missing, score = calculate_match(
        resume_skills,
        job_skills
    )

    print("\n--- MATCHED SKILLS ---")

    for skill in matched:
        print("✓", skill)

    print("\n--- MISSING SKILLS ---")

    for skill in missing:
        print("✗", skill)

    print(f"\n--- MATCH SCORE: {score:.1f}% ---")

    """

    # read resume
    resume_text = extract_text_from_pdf("resume.pdf")

    # resume skills
    resume_skills = extract_skills(resume_text)

    # read the job description
    with open("job_description.txt","r",encoding="utf-8") as file:
        job_description = file.read()

    # job description skills
    job_skills = extract_skills(job_description)

    # compare resume and job
    matched,missing,skill_score = calculate_match(
        resume_skills,
        job_skills
    )

    # text similarity
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

    # print the results
    print("RESUME JOB MATCHER")


    print("\n RESUME SKILLS")

    for skill in resume_skills:
        print("✓", skill)

    print("\n JOB SKILLS ")

    for skill in job_skills:
        print("-",skill)

    print("\n MATCHED SKILLS ")

    for skill in matched:
        print("✓", skill)

    print("\n MISSING SKILLS ")

    for skill in missing:
        print("✗", skill)

    print(f"\n Skill Match Score : {skill_score:.1f}% ")

    print(f"Text Similarity Score: {similarity_score:.1f}%")

    print(f"FINAL MATCH SCORE: {final_score:.1f}%")