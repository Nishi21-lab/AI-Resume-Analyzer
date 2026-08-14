import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_job_roles(path="data/job_roles.csv"):
    return pd.read_csv(path)

def match_resume_to_roles(resume_text, job_df):
    results = []
    for _, row in job_df.iterrows():
        role_text = row["required_skills"].replace(",", " ")
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([resume_text, role_text])
        score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        results.append({"role": row["role"], "score": round(score * 100, 2)})
    results.sort(key=lambda x: x["score"], reverse=True)
    return results