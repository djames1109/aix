from PyPDF2 import PdfReader


def get_pdf_content(file_path):
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content