from collections import Counter
from nlp_processing import extract_skill_sentences, filter_relevant_skills
import spacy

nlp = spacy.load("en_core_web_sm")  # Load spaCy here too for sentence analysis

def analyze_jobs(role, combined_df):
    role_jobs = combined_df[combined_df["Title"].str.contains(role, case=False, na=False)]
    if role_jobs.empty:
        return "No jobs found.", "", ""

    all_sentences, all_skills = [], Counter()
    for job_desc in role_jobs["Skills"]:
        if isinstance(job_desc, str):
            sentences, skills = extract_skill_sentences(job_desc)
            all_sentences.extend(sentences)
            all_skills.update(skills)

    # Get top 10 skills by frequency and filter them
    skill_counts = all_skills.most_common(10)
    initial_skills = [skill for skill, _ in skill_counts]
    filtered_skills = filter_relevant_skills(initial_skills)
    useful_skills = filter_useful_skills(filtered_skills, all_skills)

    # Filter sentences with scoring
    filtered_sentences = filter_skill_sentences(all_sentences, useful_skills)

    return "\n".join(filtered_sentences[:10]), "\n".join(useful_skills), ""

def filter_useful_skills(skills, skill_counts, min_frequency=2):
    noise_terms = {
        "that", "you", "we", "they", "it", "this", "and", "with", "in", "of", "to", "a", "an", "the",
        "is", "are", "be", "have", "on", "at", "for", "or", "as", "by", "from", "using", "ability"
    }
    
    useful = []
    for skill in skills:
        skill_lower = skill.lower()
        count = skill_counts[skill]
        if (count >= min_frequency and
            len(skill) > 2 and
            skill_lower not in noise_terms and
            not any(char in skill for char in ".;,:")):
            useful.append(skill)
    return useful

def filter_skill_sentences(sentences, useful_skills):
    skill_set = {skill.lower() for skill in useful_skills}
    noise_patterns = {"location", "duration", "contract", "job title", "remote", "office", "days", "week", "responsible to", "works as", "maintain", "milwaukee", "wi"}
    
    filtered = []
    for sentence in sentences:
        doc = nlp(sentence)
        sentence_lower = sentence.lower()
        
        # Scoring system
        score = 0
        
        # +2 for each useful skill mentioned
        for skill in skill_set:
            if skill in sentence_lower:
                score += 2
        
        # +1 for skill keywords with specific nouns after them
        for token in doc:
            if token.text.lower() in ["experience", "knowledge", "proficient", "familiarity"] and token.i + 1 < len(doc):
                next_token = doc[token.i + 1]
                if (next_token.pos_ in ("NOUN", "PROPN") and 
                    next_token.text.lower() not in {"team", "ability", "work", "skills"} and 
                    len(next_token.text) > 2):
                    score += 1
        
        # -1 for noise patterns
        for noise in noise_patterns:
            if noise in sentence_lower:
                score -= 1
        
        # -1 if too short or vague
        if len(doc) < 5:
            score -= 1
        
        # Keep if score is positive (tweak threshold as needed)
        if score > 0:
            filtered.append(sentence)
    
    return filtered