# 📄 Resume Job Matcher

A Python-based web application that analyzes a resume against a job description and helps identify how well the resume matches the job requirements.

The application extracts skills from a PDF resume, compares them with the skills required in a job description, calculates text similarity using TF-IDF and cosine similarity, and displays matched and missing skills along with an overall match score.

## 🚀 Live Demo

🔗 **Live Application:**  
https://resume-job-matcher-eh4x3dipe7hmsef6nanp8.streamlit.app/

## 📌 Project Overview

Finding out whether a resume matches a particular job description can be time-consuming.

The **Resume Job Matcher** automates this initial analysis by comparing the candidate's resume with a job description.

It provides:

- Resume skill extraction
- Job requirement analysis
- Matched skills
- Missing skills
- Skill match percentage
- Text similarity percentage
- Final match score

This project demonstrates the use of **Python, NLP techniques, machine learning concepts, Streamlit, Git, and GitHub** in a practical application.

## ✨ Features

- 📄 Upload resume in PDF format
- 🔍 Extract text from resume
- 🧠 Extract technical skills
- 💼 Compare resume with job description
- ✅ Display matched skills
- ❌ Display missing skills
- 📊 Calculate skill match score
- 📈 Calculate text similarity using TF-IDF
- 🔢 Calculate cosine similarity
- 🎯 Generate a final match score
- 🌐 Interactive Streamlit web interface
- ☁️ Deployed using Streamlit Community Cloud

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| PyPDF | Extract text from PDF resumes |
| Scikit-learn | Text processing and similarity |
| TF-IDF | Convert text into numerical features |
| Cosine Similarity | Measure text similarity |
| Git | Version control |
| GitHub | Source code hosting |
| Streamlit Community Cloud | Deployment |

## 🧠 How the Project Works

The application follows these steps:

```text
Resume PDF
    ↓
Extract Resume Text
    ↓
Extract Resume Skills
    ↓
Enter Job Description
    ↓
Extract Required Skills
    ↓
Compare Resume Skills with Job Skills
    ↓
Calculate Skill Match Score
    ↓
Calculate TF-IDF Text Similarity
    ↓
Calculate Final Match Score
    ↓
Display Results
📊 Matching Approach

The application uses two main components to analyze the resume.

1. Skill Matching

The application compares the skills found in the resume with the skills required by the job description.

For example:

Matched Skills

Python
Git
GitHub

Missing Skills

SQL
Docker
FastAPI

The skill match percentage is calculated based on the number of required skills found in the resume.

2. Text Similarity

The application uses:

TF-IDF (Term Frequency-Inverse Document Frequency)
Cosine Similarity

to measure the similarity between the resume text and the job description.

3. Final Match Score

The final score combines the skill matching result and the text similarity result to provide an overall indication of how closely the resume matches the job description.

🖥️ Example Result

Example output from the application:

Final Match Score: 23.0%

Text Similarity: 6.7%

Matched Skills:
- Python
- Git
- GitHub

Missing Skills:
- NumPy
- Pandas
- SQL
- FastAPI
- Docker

The actual score depends on the resume and job description provided by the user.

📂 Project Structure
resume-job-matcher/
│
├── app.py
├── streamlit_app.py
├── skill_extractor.py
├── job_matcher.py
├── text_similarity.py
├── job_description.txt
├── requirements.txt
├── .gitignore
└── README.md
📁 File Description
streamlit_app.py

Contains the Streamlit web interface and connects the different components of the project.

skill_extractor.py

Extracts relevant technical skills from resume and job description text.

job_matcher.py

Compares resume skills with the skills required by the job description.

text_similarity.py

Uses TF-IDF and cosine similarity to calculate text similarity between the resume and job description.

app.py

Contains the core resume processing functionality.

job_description.txt

Sample job description used for testing.

requirements.txt

Contains the Python dependencies required to run the project.

⚙️ Installation and Setup
1. Clone the repository
git clone https://github.com/ritikagoyal01/resume-job-matcher.git
2. Navigate to the project directory
cd resume-job-matcher
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

On Windows:

.venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Run the application
streamlit run streamlit_app.py

The application will open in your browser.

☁️ Deployment

The application is deployed using Streamlit Community Cloud and connected to the GitHub repository.

Live Application

https://resume-job-matcher-eh4x3dipe7hmsef6nanp8.streamlit.app/

🔒 Privacy Note

The application is designed to analyze a resume uploaded by the user during the current session.

Personal resume files should not be committed to the public GitHub repository.

🚀 Future Improvements

Some possible improvements include:

Add a larger skill database
Support skill aliases such as sklearn and scikit-learn
Improve skill extraction using advanced NLP techniques
Use semantic embeddings for better resume-job similarity
Add job recommendations
Recommend missing skills to learn
Add visual charts for match analysis
Support multiple job descriptions
Add downloadable analysis reports
🎯 Learning Outcomes

Through this project, I worked with:

Python programming
PDF text extraction
Natural Language Processing concepts
TF-IDF
Cosine similarity
Basic machine learning techniques
Streamlit application development
Git and GitHub
Virtual environments
Dependency management
Cloud deployment
👩‍💻 Author

Ritika Goyal

B.Tech Student

Skills

Python • Machine Learning • NLP • Scikit-learn • Streamlit • Git • GitHub

⭐ If you find this project useful, consider giving the repository a star!