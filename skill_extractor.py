def extract_skills(text):
    skills = [
        "Python",
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Scikit-learn",
        "OpenCV",
        "SQL",
        "Git",
        "GitHub",
        "FastAPI",
        "Docker",
        "AWS",
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    return found_skills

if __name__ == "__main__":
    resume_text = """
    I have experience with Python, Pandas, NumPy,
    Scikit-learn, OpenCV and Git.
    """

    skills = extract_skills(resume_text)

    print("Skills found:")
    
    for skill in skills:
        print("-", skill)