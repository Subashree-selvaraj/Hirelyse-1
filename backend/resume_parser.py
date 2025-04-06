import pdfplumber
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3})?[\s-]?(\d{10})', text)
    return match.group(0) if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def parse_resume(file_path):
    text = extract_text_from_pdf(file_path)
    parsed = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "text": text
    }
    return parsed
