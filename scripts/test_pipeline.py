import os
import sys
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

def test():
    print(">>> Starting Pipeline Self-Test...")
    test_dir = os.path.join(REPO_ROOT, "jobs", "test_job")
    os.makedirs(test_dir, exist_ok=True)
    
    config = {
        "summary": "Results-driven Software Engineer with extensive experience building scalable services and automation.",
        "skills_lines": [
            ["Languages", "Python, SQL, Shell Scripting"],
            ["Cloud & Databases", "AWS, PostgreSQL, Docker, Linux"]
        ],
        "experience_bullets": [
            {"lead": "Architecture & Automation", "text": "Architected automated workflows processing 1M+ daily records, slashing latency by 35%."},
            {"lead": "Query Optimization", "text": "Refactored high-latency relational queries, achieving a 40% reduction in query runtimes."}
        ],
        "project_bullets": [
            {"text": "Engineered automated data ingestion frameworks handling 1M+ records daily with 99.9% uptime."}
        ]
    }
    
    cfg_file = os.path.join(test_dir, "config.yaml")
    with open(cfg_file, "w", encoding="utf-8") as f:
        yaml.dump(config, f)
        
    render(cfg_file, test_dir)
    is_valid, errs, warns = validate_resume(os.path.join(test_dir, "resume.docx"), os.path.join(test_dir, "resume.pdf"))
    
    if is_valid:
        print("✅ Pipeline Self-Test PASSED (Strictly 1 Page ATS PDF Verified)!")
    else:
        print(f"❌ Test Failed: {errs}")

if __name__ == "__main__":
    test()
