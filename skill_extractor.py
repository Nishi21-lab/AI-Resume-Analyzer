import re
import pandas as pd

def load_skill_dictionary(path="data/skill_dictionary.csv"):
    return pd.read_csv(path)

def extract_skills(cleaned_text, skill_df):
    found = []
    for _, row in skill_df.iterrows():
        skill = row["skill"]
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, cleaned_text):
            found.append({"skill": skill, "category": row["category"]})
    return found