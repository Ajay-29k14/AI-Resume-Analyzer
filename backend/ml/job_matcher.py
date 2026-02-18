import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from embedder import get_embedding
from preprocessing import clean_text
import pandas as pd

# Load saved jobs
jobs = pd.read_csv("saved_models/processed_jobs.csv")

with open("saved_models/job_embeddings.pkl", "rb") as f:
    job_embeddings = pickle.load(f)

def match_resume(resume_text, top_k=5):
    clean_resume = clean_text(resume_text)
    resume_embedding = get_embedding(clean_resume)

    similarities = cosine_similarity(
        [resume_embedding],
        job_embeddings
    )[0]

    top_indices = similarities.argsort()[-top_k:][::-1]

    results = []
    for idx in top_indices:
        results.append({
            "job_title": jobs.iloc[idx]["Job Title"],
            "similarity_score": float(similarities[idx]),
            "match_percentage": round(float(similarities[idx]) * 100, 2)
        })


    return results
