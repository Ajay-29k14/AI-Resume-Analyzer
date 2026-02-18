import json

with open("ml/skills_master.json", "r") as f:
    SKILLS = json.load(f)


def extract_skills(text):
    text = text.lower()
    found = []

    for skill in SKILLS:
        if skill.lower() in text:
            found.append(skill)

    return found
