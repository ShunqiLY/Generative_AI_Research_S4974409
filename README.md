# Generative AI Research — S4974409

**Study Title:** Using Generative AI Tools — Boon or Bane  
**Repository Owner:** ShunqiLY  
**Institution:** The University of Queensland  
**Course:** REIT6811 — Applied Class 6  
**Last Updated:** 2026-04-29

---

## Overview

This repository contains all materials for a mixed-methods study investigating how
users perceive and adopt Generative AI tools in academic and professional settings.
The study explores benefits, challenges, ethical concerns, and integrity implications
through a combination of quantitative surveys and qualitative interviews.

---

## Repository Structure

```
Generative_AI_Research_S4974409/
├── 01_Literature_Review/
│   ├── journal_articles/       # Peer-reviewed journal papers (PDF)
│   ├── conference_articles/    # Conference proceedings (PDF)
│   ├── books/                  # Book chapters and ebooks
│   ├── newspaper_articles/     # News and media coverage
│   └── references.bib          # Master BibTeX reference list
│
├── 02_Quantitative_Analysis/
│   ├── survey_questions/       # Survey instrument versions (.txt)
│   ├── survey_data/            # Raw and cleaned survey data (.csv)
│   ├── analysis_scripts/       # Python analysis scripts (.py)
│   └── reports/                # Statistical analysis reports
│
├── 03_Qualitative_Analysis/
│   ├── interview_protocols/    # Interview guide versions (.txt)
│   ├── consent_forms/          # Signed participant consent forms
│   ├── interview_transcripts/  # De-identified interview transcripts (.txt)
│   ├── analysis_reports/       # Thematic analysis insights (.txt)
│   └── data_visualisations/    # Charts and theme maps (PNG/PDF)
│
├── 04_Drafts_and_Reports/
│   ├── research_proposals/     # Draft research proposals
│   ├── conference_papers/      # Conference paper submissions
│   └── final_reports/          # Final published reports
│
└── 05_Additional_Materials/
    ├── information_sheets/     # Participant information sheets
    ├── photos/                 # Research-related photos
    └── media_files/            # Other media and supplementary files
```

---

## Access Controls

| Folder | Sensitivity | Notes |
|--------|-------------|-------|
| `03_Qualitative_Analysis/consent_forms/` | **Restricted** | Contains signed documents — do not share publicly |
| `03_Qualitative_Analysis/interview_transcripts/` | **Restricted** | De-identified, but access limited to research team |
| `02_Quantitative_Analysis/survey_data/` | **Restricted** | Raw data — share only cleaned/aggregated versions |
| All other folders | Public (within team) | Safe to share with collaborators |

---

## File Naming Convention

Follow this pattern for all new files:

```
[category]_[descriptor]_[version or date].[extension]
```

Examples:
- `survey_data_raw_2026-04.csv`
- `interview_transcript_P002_anonymised.txt`
- `analysis_script_likert_v2.py`

Rules:
- Use **lowercase** and **underscores** (no spaces or special characters)
- Include a **version number** (v1, v2) or **date** (YYYY-MM) for iterative files
- Use **descriptive names** — avoid generic names like `data.csv` or `final.docx`

---

## How to Contribute

1. **Fork** this repository to your own GitHub account.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/Generative_AI_Research_S4974409.git
   ```
3. Create a **new branch** with a descriptive name:
   ```bash
   git checkout -b feature/add-survey-data-cleaning
   ```
4. Make your changes and **commit** with a meaningful message:
   ```bash
   git commit -m "Add cleaned survey data and Likert summary statistics"
   ```
5. **Push** your branch and open a **Pull Request** to the `main` branch.
6. The repository owner will **review** and merge your changes.

---

## Commit Message Guidelines

Write commit messages in the imperative mood and describe *what* and *why*:

| Good | Avoid |
|------|-------|
| `Add initial interview protocol v1` | `update` |
| `Fix missing values in survey_data_raw.csv` | `changes` |
| `Refactor analysis script to use pandas groupby` | `misc` |

---

## Contact

For questions about this repository or the research project, open a GitHub Issue or
contact the repository owner via GitHub: [@ShunqiLY](https://github.com/ShunqiLY)
