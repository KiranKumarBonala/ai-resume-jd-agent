import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

INDEX_FILE = Path("embeddings/docs.index")
TEXT_FILE = Path("embeddings/texts.npy")

def load_index():
    index = faiss.read_index(str(INDEX_FILE))
    texts = np.load(TEXT_FILE, allow_pickle=True)
    return index, texts

def search(query, top_k=3):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    query_vec = model.encode([query]).astype("float32")

    index, texts = load_index()
    distances, indices = index.search(query_vec, top_k)

    results = []
    for idx in indices[0]:
        results.append(texts[idx])

    return results

if __name__ == "__main__":
    query = input("Enter your query: ")
    results = search(query)

    for i, res in enumerate(results, 1):
        print(f"\n--- Result {i} ---\n")
        print(res[:500])
