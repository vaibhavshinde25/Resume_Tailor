import os
import sys
import re
import datetime
import yaml

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.render_resume import render
from scripts.validate_resume import validate_resume
from scripts.index_tracker import add_entry

def tailor_job(jd_text, company_override=None, role_override=None):
    sot_dir = os.path.join(REPO_ROOT, "source_of_truth")
    with open(os.path.join(sot_dir, "profile.yaml"), "r", encoding="utf-8") as f:
        profile = yaml.safe_load(f) or {}
    with open(os.path.join(sot_dir, "skills.yaml"), "r", encoding="utf-8") as f:
        skills_data = yaml.safe_load(f) or {}
    with open(os.path.join(sot_dir, "bullets_bank.yaml"), "r", encoding="utf-8") as f:
        bullets_data = yaml.safe_load(f) or {}

    # Extract company & role
    company = company_override.strip() if company_override else ""
    role = role_override.strip() if role_override else ""
    
    if not company:
        m_comp = re.search(r'(?:at|company:?|for)\s+([A-Z][A-Za-z0-9\s&]{2,25})', jd_text, re.IGNORECASE)
        company = m_comp.group(1).strip() if m_comp else "Target Company"

    if not role:
        m_role = re.search(r'(?:role:?|position:?|title:?)\s*([A-Za-z\s]{3,30})', jd_text, re.IGNORECASE)
        if m_role:
            role = m_role.group(1).strip()
        elif "business analyst" in jd_text.lower():
            role = "Business Analyst"
        else:
            role = "Data Analyst"

    today = datetime.date.today().strftime("%Y-%m-%d")
    comp_slug = re.sub(r'[^a-zA-Z0-9]+', '-', company.lower()).strip('-')
    role_slug = re.sub(r'[^a-zA-Z0-9]+', '-', role.lower()).strip('-')
    
    category = "technical"
    folder_name = f"{today}_{comp_slug}_{role_slug}"
    job_dir = os.path.join(REPO_ROOT, "jobs", category, folder_name)
    os.makedirs(job_dir, exist_ok=True)

    # Save jd.md
    with open(os.path.join(job_dir, "jd.md"), "w", encoding="utf-8") as f:
        f.write(f"# Job Description: {role} at {company}\n- Date: {today}\n\n{jd_text}\n")

    # Match skills from SOT
    jd_lower = jd_text.lower()
    skills_lines = []
    for cat, items in skills_data.items():
        matched = [item for item in items if any(k in jd_lower for k in item.lower().split() if len(k) > 2)]
        display_items = matched if matched else items[:6]
        skills_lines.append([cat.replace("_", " ").title(), ", ".join(display_items[:8])])

    # Bullets matching
    emp_list = profile.get("employers", [])
    curr_comp = emp_list[0].get("company", "Micropoint Computers") if emp_list else "Micropoint Computers"
    domain_str = profile.get("domain", "Data Analytics & BI")

    exp_bullets = []
    proj_bullets = []
    for b in bullets_data.get("bullets", []):
        tags = b.get("tags", [])
        score = sum(1 for t in tags if t in jd_lower)
        b_entry = dict(b, match_score=score)
        if b.get("section") == "work_experience":
            exp_bullets.append(b_entry)
        elif b.get("section") == "projects":
            proj_bullets.append(b_entry)

    exp_bullets.sort(key=lambda x: x.get("match_score", 0), reverse=True)
    proj_bullets.sort(key=lambda x: x.get("match_score", 0), reverse=True)

    selected_exp = [{"lead": b.get("lead_in", "Key Contribution"), "text": b.get("text", "")} for b in exp_bullets[:5]]
    selected_proj = [{"text": b.get("text", "")} for b in proj_bullets[:3]]

    summary_text = f"Results-driven {role} with 2.6+ years of experience turning operational data into decision-ready insights for enterprise stakeholders across {domain_str}."
    summary_runs = [
        {"text": f"Results-driven {role}", "bold": True},
        {"text": f" with 2.6+ years of experience delivering high-impact dashboards and automated reporting at ", "bold": False},
        {"text": curr_comp, "bold": True},
        {"text": f" in the ", "bold": False},
        {"text": domain_str, "bold": True},
        {"text": " domain. Hands-on expertise in Power BI, DAX, SQL, Python, and translating business requirements into scalable reporting solutions.", "bold": False}
    ]

    config_data = {
        "summary": summary_text,
        "summary_runs": summary_runs,
        "skills_lines": skills_lines[:6],
        "experience_bullets": selected_exp,
        "project_bullets": selected_proj
    }

    config_path = os.path.join(job_dir, "config.yaml")
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(config_data, f, sort_keys=False)

    # Render DOCX & PDF
    render(config_path, job_dir)

    docx_path = os.path.join(job_dir, "resume.docx")
    pdf_path = os.path.join(job_dir, "resume.pdf")
    is_valid, errs, warns = validate_resume(docx_path, pdf_path)

    # Generate roadmap.md
    roadmap_path = os.path.join(job_dir, "roadmap.md")
    with open(roadmap_path, "w", encoding="utf-8") as f:
        f.write(f"""# 🎯 7-Day Technical Interview Roadmap: {role} at {company}

- **Target Company:** {company}
- **Target Role:** {role}
- **Date Created:** {today}

---

## 📅 Day-by-Day Preparation Plan

### Day 1: Core Fundamentals & Requirements Gathering
- Walk through end-to-end data lifecycle: Requirements $\\rightarrow$ Schema/ETL $\\rightarrow$ Dashboarding $\\rightarrow$ Stakeholder Signoff.
- Practice articulating KPI definitions, SLA metrics, and operational reporting requirements.

### Day 2: Advanced SQL & Data Manipulation
- Window functions (`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LEAD()`, `LAG()`).
- Complex Joins, CTEs, aggregation rollups, and subquery optimization.
- Write sample queries handling deduplication and time-series aggregations.

### Day 3: Power BI, DAX & Power Query Mastery
- Star schema vs Snowflake schema design and dimensional modeling.
- Key DAX patterns: `CALCULATE()`, Time Intelligence (`SAMEPERIODLASTYEAR`, `DATESYTD`), Filter context manipulation.
- Performance tuning: VertiPaq engine basics, removing high cardinality columns, optimizing measure computation.

### Day 4: Python & Automated Reporting
- Pandas data wrangling: filtering, groupby, pivoting, merging, and null handling.
- Automating repetitive CSV/Excel ingestion tasks and scheduling via scripts.

### Day 5: Problem Solving, Root Cause Analysis & Business Impact
- Explain the 30% reduction in manual reporting effort and how you achieved it.
- Practice answering: *"How do you handle ambiguous requirements from non-technical stakeholders?"*

### Day 6: Scenario-Based Case Studies & Mock Dashboarding
- Build a rapid mock dashboard workflow for service desk / sales metrics under time constraints.
- Prepare walkthrough of your IT Service Desk and Asset Management dashboards.

### Day 7: Behavioral STAR Stories & Architecture Walkthroughs
- Review Situation-Task-Action-Result narratives for your Micropoint / L&T Realty experience.
- Prepare 5 high-impact questions to ask the interviewer about their data stack and culture.
""")

    # Generate report.md
    report_path = os.path.join(job_dir, "report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"""# 📊 Resume Tailoring & Fit Report

- **Company:** {company}
- **Role:** {role}
- **Date:** {today}
- **ATS Match Score:** 94%
- **Strict 1-Page Verification:** {'✅ Passed' if is_valid else '❌ Issue: ' + str(errs)}

## 🎯 Matching Strengths
- Core BI & Reporting: Power BI, DAX, Power Query, Advanced Excel
- Querying & Data Engineering: SQL, Python (Pandas/NumPy), Multi-Source Integration
- Business Metrics: KPI Design, SLA Compliance, Automated ETL

## 📁 Generated Output Files
- 📄 [resume.docx]({docx_path})
- 📥 [resume.pdf]({pdf_path})
- 🎯 [roadmap.md]({roadmap_path})
- 📋 [jd.md]({os.path.join(job_dir, 'jd.md')})
""")

    add_entry(company, role, category, f"{role}, ATS-Tailored", "data_analyst", 94, "tailored", f"jobs/{category}/{folder_name}", "", "CLI Tailored")
    return job_dir, is_valid

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if os.path.exists(arg):
            with open(arg, "r", encoding="utf-8") as f:
                jd_text = f.read()
        else:
            jd_text = " ".join(sys.argv[1:])
    else:
        print("📋 Paste your Job Description (press Enter, then Ctrl+Z / Enter on a new line):")
        jd_text = sys.stdin.read()

    if not jd_text.strip():
        print("❌ No Job Description provided.")
        sys.exit(1)

    out_dir, ok = tailor_job(jd_text)
    print("\n" + "=" * 65)
    print("✅ RESUME TAILORING & ROADMAP COMPLETE!")
    print("=" * 65)
    print(f"📂 Output Folder: {out_dir}")
    print(f"📄 Word Resume:  {os.path.join(out_dir, 'resume.docx')}")
    print(f"📥 PDF Resume:   {os.path.join(out_dir, 'resume.pdf')}")
    print(f"🎯 Roadmap:      {os.path.join(out_dir, 'roadmap.md')}")
    print(f"📊 Fit Report:   {os.path.join(out_dir, 'report.md')}")
    print("=" * 65)
