# Smart Resume Analyzer

A simple Python tool to analyze PDF resumes and match skills against a job requirement list.

## Features

* Extract text from PDF resumes using `pdfplumber`
* Clean and process text
* Compare keywords with required skills
* Display match percentage, matched and missing skills

## Requirements

```bash
pip install pdfplumber nltk
python -m nltk.downloader stopwords
```

## Usage

```bash
python ai_based_resume_analyzer.py
```

Enter the resume filename when prompted.

---

## Author

Created by **Arati Kadam**.
