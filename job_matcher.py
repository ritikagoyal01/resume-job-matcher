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