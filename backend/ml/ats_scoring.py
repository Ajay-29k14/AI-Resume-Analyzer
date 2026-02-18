import re

def calculate_ats_score(similarity_score, resume_text, required_skills):
    resume_text = resume_text.lower()

    # Skill coverage
    matched_skills = [skill for skill in required_skills if skill.lower() in resume_text]
    skill_score = len(matched_skills) / len(required_skills) if required_skills else 0

    # Experience detection
    experience_score = 1 if re.search(r"\b(year|experience)\b", resume_text) else 0

    # Education detection
    education_score = 1 if re.search(r"\b(bachelor|master|phd|degree)\b", resume_text) else 0

    # Weighted ATS score
    ats_score = (
        0.4 * similarity_score +
        0.3 * skill_score +
        0.15 * experience_score +
        0.15 * education_score
    )

    return round(ats_score * 100, 2)
