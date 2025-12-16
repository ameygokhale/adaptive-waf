import subprocess
import sys
import os
import time

# ------------------------------------------------------------
# Helper function to run Python scripts in separate processes
# ------------------------------------------------------------

def run_script(path):
    print(f"[+] Starting: {path}")
    return subprocess.Popen([sys.executable, path])


# ------------------------------------------------------------
# MAIN RUNNER
# ------------------------------------------------------------

if __name__ == "__main__":
    print("\n===============================================")
    print("   ADAPTIVE WAF – FULL SYSTEM AUTO STARTER")
    print("===============================================\n")

    base = os.path.dirname(os.path.abspath(__file__))

    # Paths
    backend_path = os.path.join(base, "backend_app", "server.py")
    waf_path = os.path.join(base, "scripts", "run_waf.py")
    dashboard_path = os.path.join(base, "dashboard", "app.py")
    pipeline_path = os.path.join(base, "scripts", "pipeline.py")

    # --------------------------------------------------------
    # START COMPONENTS
    # --------------------------------------------------------

    print("[1] Starting backend server (port 9000)...")
    backend_process = run_script(backend_path)
    time.sleep(1)

    print("[2] Starting WAF (port 8080)...")
    waf_process = run_script(waf_path)
    time.sleep(1)

    print("[3] Starting dashboard (port 8090)...")
    dashboard_process = run_script(dashboard_path)
    time.sleep(1)

    print("[4] Starting recon + rule engine pipeline...")
    pipeline_process = run_script(pipeline_path)
    time.sleep(1)

    print("\n===============================================")
    print(" ALL SYSTEMS RUNNING SUCCESSFULLY 🎉")
    print("===============================================\n")

    print("🔹 Backend:   http://localhost:9000")
    print("🔹 WAF:       http://localhost:8080")
    print("🔹 Dashboard: http://localhost:8090")
    print("\n(Press CTRL + C to stop all processes)\n")

    # --------------------------------------------------------
    # KEEP SCRIPT ALIVE
    # --------------------------------------------------------
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Shutting down all processes...")
        backend_process.terminate()
        waf_process.terminate()
        dashboard_process.terminate()
        pipeline_process.terminate()
        print("[✔] All processes stopped. Goodbye!\n")
