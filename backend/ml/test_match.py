import pandas as pd
from job_matcher import match_resume

# Load one resume
resumes = pd.read_csv("data/Resume.csv")

sample_resume = resumes.iloc[0]["Resume_str"]

results = match_resume(sample_resume)

print(results)
