
from flask import Flask, request, Response
import json
from middleware import apply_rules
from logger import log, init_db

app = Flask(__name__)
init_db()

def load_rules():
    try:
        with open("rule_engine/rule_store.json") as f:
            return json.load(f)
    except:
        return {"block_patterns": [], "restricted_paths": [], "rate_limit": {}}

@app.before_request
def waf_filter():
    rules = load_rules()
    decision = apply_rules(request, rules)
    ip = request.remote_addr
    path = request.path

    if decision["blocked"]:
        log(ip, path, "BLOCKED", decision["reason"])
        return Response("Blocked by WAF", status=403)

    log(ip, path, "ALLOWED")
    return None

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def backend(path):
    return f"WAF passed → backend received: /{path}"

if __name__ == "__main__":
    app.run(port=8080)
