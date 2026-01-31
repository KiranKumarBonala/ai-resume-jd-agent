from pathlib import Path
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_FILE = Path("data/documents.txt")
INDEX_DIR = Path("embeddings")
INDEX_FILE = INDEX_DIR / "docs.index"
TEXT_FILE = INDEX_DIR / "texts.npy"

def load_documents():
    if not DATA_FILE.exists():
        raise FileNotFoundError("documents.txt not found. Run ingest.py first.")
    return DATA_FILE.read_text(encoding="utf-8").split("\n\n---\n\n")

def build_index(texts):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    return index, embeddings

def save_index(index, texts):
    INDEX_DIR.mkdir(exist_ok=True)
    faiss.write_index(index, str(INDEX_FILE))
    np.save(TEXT_FILE, texts)

def main():
    texts = load_documents()
    index, _ = build_index(texts)
    save_index(index, texts)
    print("EMBEDDING_OK")

if __name__ == "__main__":
    main()
