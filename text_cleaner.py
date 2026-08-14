import re

def clean_text(text):
    text = text.lower()
    text = text.replace("c++", "cplusplus").replace("c#", "csharp")
    text = re.sub(r"[^a-z0-9\s.]", " ", text)
    text = text.replace("cplusplus", "c++").replace("csharp", "c#")
    text = re.sub(r"\s+", " ", text).strip()
    return text