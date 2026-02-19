from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from ml.resume_parser import extract_text
from ml.skill_extractor import extract_skills
from ml.preprocessing import clean_text
import re


async def analyze_resume(file, job_description):
    # 1️⃣ Extract resume text
    resume_text = extract_text(file)

    # 2️⃣ Clean text
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_description)

    # 3️⃣ TF-IDF Vectorization
    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform([clean_resume, clean_job])

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    match_percentage = round(float(similarity) * 100, 2)

    # 4️⃣ Skill Extraction
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    skill_coverage = (
        len(matched_skills) / len(job_skills)
        if job_skills else 0
    )

    # 5️⃣ Basic ATS Score Calculation
    ats_score = round(
        (match_percentage * 0.6) +
        (skill_coverage * 100 * 0.4),
        2
    )

    # 6️⃣ Verdict Logic (based on ATS score)
    if ats_score >= 75:
        verdict = "Strong Fit"
    elif ats_score >= 60:
        verdict = "Moderate Fit"
    else:
        verdict = "Weak Fit"

    return {
        "match_percentage": match_percentage,
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "verdict": verdict
    }
