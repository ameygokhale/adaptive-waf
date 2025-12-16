
from flask import Flask, render_template
import sqlite3
import os
base = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(base, "..", "waf", "logs.db")



app = Flask(__name__)

@app.route("/")
def logs():
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT timestamp, ip, path, status, reason FROM waf_logs ORDER BY id DESC")
    rows = cur.fetchall()
    conn.close()
    return render_template("dashboard.html", logs=rows)

if __name__ == "__main__":
    app.run(port=8090)
