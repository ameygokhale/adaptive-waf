
import sqlite3, time

def init_db():
    conn = sqlite3.connect("waf/logs.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS waf_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp INTEGER,
            ip TEXT,
            path TEXT,
            status TEXT,
            reason TEXT
        )
    """)
    conn.commit()
    conn.close()

def log(ip, path, status, reason=""):
    conn = sqlite3.connect("waf/logs.db")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO waf_logs (timestamp, ip, path, status, reason) VALUES (?, ?, ?, ?, ?)",
        (int(time.time()), ip, path, status, reason)
    )
    conn.commit()
    conn.close()
