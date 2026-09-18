from pypdf import PdfReader
from skill_extractor import extract_skills


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text =""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text +"\n"

    return text

if __name__ == "__main__":
    pdf_path = input("enter the path to your resume pdf: ")

    text = extract_text_from_pdf(pdf_path)

    print("\n ---EXTRACTED RSEUME TEXT ---\n")
    print(text)

    skills = extract_skills(text)

    print("\n---SKILLS FOUND---\n")

    for skill in skills:
        print("-",skill)