import spacy
from collections import Counter
from fuzzywuzzy import fuzz

nlp = spacy.load("en_core_web_sm")

STOPWORDS = {"requirements", "skills", "years", "team", "development", "solutions", "systems", "tools"}
SKILL_KEYWORDS = ["experience with", "knowledge of", "proficient in", "familiarity with"]

def extract_skill_sentences(text):
    doc = nlp(text)
    sentences, skill_terms = [], []

    for sent in doc.sents:
        if any(keyword in sent.text.lower() for keyword in SKILL_KEYWORDS):
            sentences.append(sent.text.strip())
            skill_terms.extend(chunk.text.strip() for chunk in sent.noun_chunks if chunk.text.lower() not in STOPWORDS)
    
    return sentences, normalize_skills(skill_terms)

def normalize_skills(skills):
    normalized = []
    for skill in skills:
        if not any(fuzz.ratio(skill.lower(), norm.lower()) > 85 for norm in normalized):
            normalized.append(skill)
    return normalized

def filter_relevant_skills(skills):
    generic_terms = {"skills", "tools", "years", "experience", "development", "team"}
    return [skill for skill in skills if all(term not in skill.lower() for term in generic_terms)]