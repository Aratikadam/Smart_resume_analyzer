# ===== SMART SKILL-BASED RESUME ANALYZER =====

import pdfplumber
import re
import nltk
from nltk.corpus import stopwords

# Download stopwords (run once)
nltk.download('stopwords')

# -------- PDF TEXT EXTRACTION --------
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text


# -------- TEXT CLEANING --------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


# -------- SKILL EXTRACTION --------
def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words = text.split()
    keywords = [word for word in words if word not in stop_words and len(word) > 2]
    return set(keywords)


# -------- MAIN PROGRAM --------

file_name = input("Enter resume PDF file name (with .pdf extension): ")

try:
    resume_text = extract_text_from_pdf(file_name)
except:
    print("Error reading PDF file. Check file name.")
    exit()


# ✅ JOB REQUIRED SKILLS (ONLY SKILLS)
required_skills = """
python
sql
database
mysql
web development
problem solving
data structures
oops
"""

# Clean text
resume_text = clean_text(resume_text)
required_skills = clean_text(required_skills)

# Extract keywords
resume_keywords = extract_keywords(resume_text)
job_keywords = extract_keywords(required_skills)

# Find matched skills
matched_skills = resume_keywords.intersection(job_keywords)

# Calculate match %
if len(job_keywords) > 0:
    match_percentage = round((len(matched_skills) / len(job_keywords)) * 100, 2)
else:
    match_percentage = 0


# -------- OUTPUT --------
print("\n====== RESULTS ======")
print("Match Percentage:", match_percentage, "%")

print("\nMatched Skills:")
for skill in matched_skills:
    print("-", skill)

print("\nMissing Skills:")
for skill in job_keywords - matched_skills:
    print("-", skill)