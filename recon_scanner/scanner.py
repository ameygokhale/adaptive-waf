
import requests
from bs4 import BeautifulSoup

SAFE_DIRECTORIES = ["admin", "backup", "test", "old", "dev"]
OUTDATED_JS_SIGNATURES = ["jquery-1.", "angular-1.", "bootstrap-2.", "vue-1."]

def run_recon(target_url):
    findings = {
        "headers": {},
        "outdated_js": [],
        "open_directories": [],
        "exposed_admin_panels": []
    }

    try:
        r = requests.get(target_url, timeout=5)
        findings["headers"] = dict(r.headers)
        html = r.text
    except:
        return findings

    soup = BeautifulSoup(html, "html.parser")

    for script in soup.find_all("script"):
        src = script.get("src", "")
        if any(sig in src for sig in OUTDATED_JS_SIGNATURES):
            findings["outdated_js"].append(src)

    for d in SAFE_DIRECTORIES:
        url = f"{target_url.rstrip('/')}/{d}/"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                findings["open_directories"].append(f"/{d}/")
                if d == "admin":
                    findings["exposed_admin_panels"].append(f"/{d}/")
        except:
            pass

    return findings
