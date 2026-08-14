# AI Resume Analyzer & Job Recommendation System

An AI-powered web application that analyzes resumes, matches them against job roles, identifies skill gaps, and generates a personalized learning roadmap along with a downloadable PDF report.

## Features

- Upload resumes in PDF or DOCX format
- Automatic skill extraction using a predefined skill dictionary
- Job-role matching using TF-IDF and cosine similarity
- Match score visualization (bar chart)
- Skill gap analysis for a selected target role
- Personalized week-by-week learning roadmap
- Downloadable PDF report with all results

## Tech Stack

- Python
- Streamlit (web interface)
- scikit-learn (TF-IDF + cosine similarity)
- Plotly (visualizations)
- FPDF2 (PDF report generation)
- pypdf & python-docx (resume text extraction)

## Project Structure

```
AI_resume_ananalyser/
│
├── app.py                     # Main Streamlit application
├── resume_parser.py           # Extracts text from PDF/DOCX resumes
├── text_cleaner.py            # Cleans and normalizes extracted text
├── skill_extractor.py         # Extracts skills using skill dictionary
├── job_matcher.py              # Matches resume to job roles (TF-IDF)
├── roadmap_generator.py       # Skill gap analysis + learning roadmap
├── report_generator.py        # Generates downloadable PDF report
│
├── data/
│   ├── job_roles.csv          # Job roles and their required skills
│   └── skill_dictionary.csv   # Master list of skills by category
│
├── sample_resume/             # Sample resumes for testing
├── tests/
│   └── test_cases.csv         # Testing sheet for match accuracy
├── reports/                   # Generated chart/report assets
├── requirements.txt           # Python dependencies
└── README.md
```

## Setup Instructions

1. **Clone the repository**
```bash
   git clone https://github.com/Nishi21-lab/AI-Resume-Analyzer.git
   cd AI-Resume-Analyzer
```

2. **Create a virtual environment**
```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Run the application**
```bash
   streamlit run app.py
```

5. Open the local URL shown in the terminal (usually `http://localhost:8501`) in your browser.

## Usage

1. Upload your resume (PDF or DOCX) on the home page.
2. View the skills automatically extracted from your resume.
3. Check your match scores against different job roles.
4. Select a target role to see your skill gap analysis.
5. Follow the generated learning roadmap to fill the gaps.
6. Download the full analysis as a PDF report.

## Author

Nishitha — B.Tech CSE, 3rd Year, GITAM University