import os
import csv
import pandas as pd

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TRACKER_CSV = os.path.join(REPO_ROOT, "tracker.csv")
INDEX_MD = os.path.join(REPO_ROOT, "jobs", "_INDEX.md")

def load_tracker():
    if not os.path.exists(TRACKER_CSV):
        return pd.DataFrame()
    return pd.read_csv(TRACKER_CSV)

def add_entry(company, role, category, tags, resume_type, fit_pct, status, folder_path, job_link="", notes=""):
    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    file_exists = os.path.exists(TRACKER_CSV)
    
    with open(TRACKER_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists or os.path.getsize(TRACKER_CSV) == 0:
            writer.writerow(["date","company","role","category","tags","resume_type","fit_pct","status","folder_path","job_link","notes"])
        writer.writerow([today, company, role, category, tags, resume_type, fit_pct, status, folder_path, job_link, notes])
        
    update_index_md()

def update_index_md():
    df = load_tracker()
    if df.empty:
        return
    with open(INDEX_MD, "w", encoding="utf-8") as f:
        f.write("# Job Applications Index\n\n")
        f.write("| Date | Company | Role | Fit % | Status | Resume Folder |\n")
        f.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")
        for _, row in df.iterrows():
            f.write(f"| {row['date']} | **{row['company']}** | {row['role']} | {row['fit_pct']}% | `{row['status']}` | [{row['folder_path']}]({row['folder_path']}) |\n")
