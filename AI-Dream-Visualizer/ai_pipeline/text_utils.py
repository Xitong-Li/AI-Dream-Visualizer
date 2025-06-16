import spacy

# Load spaCy English model once
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text, num_keywords=4):
    doc = nlp(text)
    keywords = [token.text for token in doc if token.pos_ == "NOUN"]
    if len(keywords) < num_keywords:
        keywords += [token.text for token in doc if token.pos_ in ["ADJ", "PROPN"]]
    return keywords[:num_keywords]

def get_emotion_category(x, y):
    if x < 0.33:
        return "horror"
    elif x < 0.66:
        return "fantasy"
    else:
        return "healing"
