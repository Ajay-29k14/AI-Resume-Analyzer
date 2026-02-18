import asyncio
from ml.resume_parser import extract_text
from ml.preprocessing import clean_text
from ml.embedder import get_embedding
from ml.skill_extractor import extract_skills
from ml.ats_scoring import calculate_ats_score
from sklearn.metrics.pairwise import cosine_similarity


async def analyze_resume(file, job_description):

    # 1️⃣ Extract resume text
    resume_text = extract_text(file)

    # 2️⃣ Clean text
    clean_resume = clean_text(resume_text)
    clean_job = clean_text(job_description)

    # 3️⃣ Generate embeddings
    resume_embedding = get_embedding([clean_resume])[0]
    job_embedding = get_embedding([clean_job])[0]

    # 4️⃣ Similarity
    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    match_percentage = round(float(similarity) * 160, 2)

    # 5️⃣ Skill Extraction
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    skill_coverage = len(matched_skills) / len(job_skills) if job_skills else 0

    # 6️⃣ ATS Score
    ats_score = calculate_ats_score(
        similarity,
        resume_text,
        job_skills
    )

    # 7️⃣ Verdict
    if match_percentage >= 80:
        verdict = "Strong Fit"
    elif match_percentage >= 60:
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
