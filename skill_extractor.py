import re


def extract_skills(text):

    """
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
    """

    skill_aliases = {
        "Python": ["python"],
        "NumPy": ["numpy"],
        "Pandas": ["pandas"],
        "Matplotlib": ["matplotlib"],
        "Scikit-learn": ["scikit-learn", "sklearn"],
        "OpenCV": ["opencv", "cv2"],
        "SQL": ["sql"],
        "PostgreSQL": ["postgresql", "postgres"],
        "Git": ["git"],
        "GitHub": ["github"],
        "FastAPI": ["fastapi"],
        "Flask": ["flask"],
        "Docker": ["docker"],
        "AWS": ["aws", "amazon web services"],
        "JavaScript": ["javascript", "js"],
        "Machine Learning": ["machine learning", "ml"],
        "REST API": ["rest api", "rest apis", "restful api"],
    }

    found_skills = []

    text = text.lower()

    for skill , aliases in skill_aliases.items():
        for alias in aliases:
            # if alias in text:
            if re.search(r"\b"+re.escape(alias)+ r"\b",text):
                found_skills.append(skill)
                break

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