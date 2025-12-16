
from recon_scanner.scanner import run_recon
import json

TARGET_URL = "https://example.com"

data = run_recon(TARGET_URL)

with open("recon_scanner/output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Recon results saved.")
