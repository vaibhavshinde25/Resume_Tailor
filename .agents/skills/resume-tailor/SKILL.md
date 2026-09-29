---
name: resume-tailor
description: >-
  Triggered when the user types "tailor", "jd", or pastes a Job Description to tailor their ATS resume and interview roadmap.
---

# Resume Tailoring Workflow

Whenever the user provides a Job Description with the trigger word `tailor`:
1. Parse the target role, company, and technical requirements from the JD.
2. Select verified matching skills from `source_of_truth/skills.yaml`.
3. Select pre-approved metric bullets from `source_of_truth/bullets_bank.yaml`.
4. Render `resume.docx` and ATS-compliant `resume.pdf` (strictly 1 page) using `scripts/render_resume.py`.
5. Run anti-hallucination validation via `scripts/validate_resume.py`.
6. Generate `report.md` with fit score and gap analysis.
7. Generate dedicated `roadmap.md` in the job folder with company-specific 7-day preparation roadmap and interview questions.
8. Update `tracker.csv` and `jobs/_INDEX.md`.
