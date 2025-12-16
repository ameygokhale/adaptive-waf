import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from recon_scanner.scanner import run_recon
from rule_engine.generator import generate_rules, save_rules
from rule_engine.modsec_generator import generate_modsec_rules, save_modsec_rules

TARGET_URL = "https://example.com"

def pipeline():
    while True:
        findings = run_recon(TARGET_URL)
        rules = generate_rules(findings)
        save_rules(rules)

        modsec_rules = generate_modsec_rules(findings)
        save_modsec_rules(modsec_rules)

        print("[+] Pipeline cycle complete")
        time.sleep(60)

if __name__ == "__main__":
    pipeline()
