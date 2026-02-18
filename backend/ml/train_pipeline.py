import pandas as pd
import numpy as np
import pickle
from preprocessing import clean_text
from embedder import get_embedding

# 1️⃣ Load dataset (limit first for testing)
jobs = pd.read_csv("data/jobs.csv").head(500)

# 2️⃣ Remove duplicate job titles
jobs = jobs.drop_duplicates(subset=["Job Title"])

# 3️⃣ Combine title + description
jobs["full_text"] = jobs["Job Title"] + " " + jobs["Job Description"]

# 4️⃣ Clean text
jobs["clean_text"] = jobs["full_text"].apply(clean_text)

# 5️⃣ Generate embeddings (BATCH — IMPORTANT)
job_embeddings = get_embedding(list(jobs["clean_text"]))

# 6️⃣ Save embeddings
with open("saved_models/job_embeddings.pkl", "wb") as f:
    pickle.dump(job_embeddings, f)

# 7️⃣ Save processed jobs
jobs.to_csv("saved_models/processed_jobs.csv", index=False)

print("Job embeddings saved successfully.")
