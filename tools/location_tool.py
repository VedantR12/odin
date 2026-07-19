import spacy

nlp = spacy.load("en_core_web_sm")

def extract_city(text):

    doc = nlp(text)

    for ent in doc.ents:

        if ent.label_ in ["GPE", "LOC"]:

            return ent.text

    return "Delhi"