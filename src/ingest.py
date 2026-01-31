from pathlib import Path
from pypdf import PdfReader

DATA_DIR = Path("data")
RESUME_DIR = DATA_DIR / "resumes"
JD_DIR = DATA_DIR / "job_descriptions"
OUTPUT_FILE = DATA_DIR / "documents.txt"


def read_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(pdf_path)
    text = []
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)


def ingest_pdfs():
    documents = []

    for folder in [RESUME_DIR, JD_DIR]:
        for pdf in folder.glob("*.pdf"):
            content = read_pdf_text(pdf)
            if content.strip():
                documents.append(f"{pdf.name}\n{content}")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n\n---\n\n".join(documents), encoding="utf-8")


if __name__ == "__main__":
    ingest_pdfs()
