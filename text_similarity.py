from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text,job_description):
    documents = [resume_text,job_description]

    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity[0][0]*100

    return score

if __name__ == "__main__":

    resume_text ="""I am a Python developer.I have experience building backend applications,REST APIs and working with Git."""

    job_description = """We are looking for a Python developer with experience in backend development, API development and Git."""

    score = calculate_similarity(
        resume_text,
        job_description
    )

    print(f"Text Similarity Score: {score:.1f}%")