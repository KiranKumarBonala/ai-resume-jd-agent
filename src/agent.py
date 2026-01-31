from search import search

def match_resume(job_description):
    results = search(job_description, top_k=3)

    response = []
    for i, res in enumerate(results, 1):
        response.append(f"Candidate {i} Match Summary:\n{res[:600]}")

    return "\n\n".join(response)

if __name__ == "__main__":
    jd = input("Paste Job Description:\n")
    output = match_resume(jd)
    print("\n=== MATCH RESULTS ===\n")
    print(output)
