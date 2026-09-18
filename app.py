from pypdf import PdfReader

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