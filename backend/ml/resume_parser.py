import pdfplumber
from docx import Document
import tempfile


def extract_text(upload_file):
    suffix = upload_file.filename.split(".")[-1].lower()

    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{suffix}") as tmp:
        tmp.write(upload_file.file.read())
        tmp_path = tmp.name

    if suffix == "pdf":
        text = ""
        with pdfplumber.open(tmp_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    elif suffix == "docx":
        doc = Document(tmp_path)
        return "\n".join([para.text for para in doc.paragraphs])

    else:
        return ""
