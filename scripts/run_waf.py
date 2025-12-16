
import subprocess

print("[+] Starting WAF (port 8080)...")
subprocess.run(["python", "waf/app.py"])
