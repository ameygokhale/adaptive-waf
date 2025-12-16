
import json

def generate_rules(findings):
    rules = {"block_patterns": [], "restricted_paths": [], "rate_limit": {}}

    if findings["outdated_js"]:
        rules["block_patterns"].extend(["<script>", "javascript:"])

    for d in findings["open_directories"]:
        rules["restricted_paths"].append(d)

    if "/admin/" in findings["exposed_admin_panels"]:
        rules["rate_limit"]["admin"] = 10

    return rules

def save_rules(rules, path="rule_engine/rule_store.json"):
    with open(path, "w") as f:
        json.dump(rules, f, indent=4)
