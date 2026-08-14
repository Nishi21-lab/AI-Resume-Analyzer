def skill_gap_analysis(found_skills, required_skills_str):
    required = set(s.strip() for s in required_skills_str.split(","))
    found = set(item["skill"] for item in found_skills)
    matched = found & required
    missing = required - found
    return matched, missing

LEARNING_RESOURCES = {
    "docker": "Docker basics - containerization fundamentals",
    "fastapi": "FastAPI crash course - build a REST API",
    "sql": "SQL fundamentals - joins, aggregations",
    "mlflow": "MLflow basics - experiment tracking",
    "power bi": "Power BI fundamentals - dashboards",
}

def generate_roadmap(missing_skills):
    if not missing_skills:
        return ["No roadmap required — your resume already covers all the skills for this role!"]
    roadmap = []
    for i, skill in enumerate(missing_skills, start=1):
        topic = LEARNING_RESOURCES.get(skill, f"Learn {skill} basics")
        roadmap.append(f"Week {i}: {topic}")
    return roadmap