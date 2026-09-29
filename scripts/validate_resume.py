import os
import yaml
import docx
import pypdf

def load_source_of_truth():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sot_dir = os.path.join(base_dir, "source_of_truth")
    
    with open(os.path.join(sot_dir, "profile.yaml"), "r", encoding="utf-8") as f:
        profile = yaml.safe_load(f) or {}
    with open(os.path.join(sot_dir, "skills.yaml"), "r", encoding="utf-8") as f:
        skills_data = yaml.safe_load(f) or {}
    with open(os.path.join(sot_dir, "bullets_bank.yaml"), "r", encoding="utf-8") as f:
        bullets_data = yaml.safe_load(f) or {}
    with open(os.path.join(sot_dir, "certs_projects.yaml"), "r", encoding="utf-8") as f:
        certs_proj = yaml.safe_load(f) or {}

    return profile, skills_data, bullets_data, certs_proj

def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    full_text = []
    for p in doc.paragraphs:
        if p.text.strip():
            full_text.append(p.text.strip())
    return "\n".join(full_text)

def validate_resume(docx_path, pdf_path=None):
    if not os.path.exists(docx_path):
        return False, [f"DOCX file does not exist: {docx_path}"], []
    
    if pdf_path and os.path.exists(pdf_path):
        try:
            reader = pypdf.PdfReader(pdf_path)
            num_pages = len(reader.pages)
            if num_pages > 1:
                return False, [f"Strict 1-page violation: PDF has {num_pages} pages!"], []
        except Exception:
            pass

    return True, [], []
