import os
import sys
import yaml

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOT_DIR = os.path.join(REPO_ROOT, "source_of_truth")

def prompt(msg, default=""):
    val = input(f"{msg} [{default}]: ").strip()
    return val if val else default

def setup_candidate():
    print("=" * 65)
    print("   🚀 RESUME TAILOR - CANDIDATE SETUP WIZARD")
    print("=" * 65)

    name = prompt("1. Full Name", "Alex Morgan")
    email = prompt("2. Email Address", "alex.morgan@example.com")
    phone = prompt("3. Phone Number", "+91 9876543210")
    location = prompt("4. Current Location (City, State, Country)", "Bangalore, Karnataka, India")
    linkedin = prompt("5. LinkedIn profile handle/URL", "linkedin.com/in/alexmorgan")
    company = prompt("6. Current / Most Recent Company", "TechCorp Solutions")
    designation = prompt("7. Official Designation", "Software Engineer")
    functional_title = prompt("8. Functional Resume Title", "Software Engineer")
    client = prompt("9. Client / Project Name (optional)", "Global Retail Partner")
    domain = prompt("10. Industry / Domain", "Enterprise Software")

    profile_data = {
        "name": name.upper(),
        "contact": {
            "email": email,
            "phone": phone,
            "location": location,
            "linkedin": linkedin,
            "location_de": location,
            "location_dba": location,
            "linkedin_de": linkedin,
            "linkedin_dba": linkedin
        },
        "employers": [
            {
                "company": company,
                "official_designation": designation,
                "titles": {"de": functional_title, "dba": "Database Engineer"},
                "client": client,
                "project_de": f"{client} Platform" if client else "Core Platform",
                "project_dba": "Database Operations",
                "location": location.split(",")[0].strip() + ", India",
                "start_date": "Jun 2023",
                "end_date": "Present"
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Technology in Computer Science (B.Tech)",
                "institution": "National Institute of Technology",
                "dates": "2019 – 2023",
                "cgpa": "8.8 / 10.0"
            }
        ],
        "domain": domain
    }

    os.makedirs(SOT_DIR, exist_ok=True)
    with open(os.path.join(SOT_DIR, "profile.yaml"), "w", encoding="utf-8") as f:
        yaml.dump(profile_data, f, sort_keys=False)

    print("\n✅ Saved: source_of_truth/profile.yaml")

if __name__ == "__main__":
    setup_candidate()
