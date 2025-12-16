
def generate_modsec_rules(findings):
    rules = []

    if findings["outdated_js"]:
        rules.append('SecRule ARGS "@contains <script>" "id:1001,deny,status:403"')

    for d in findings["open_directories"]:
        rules.append(f'SecRule REQUEST_URI "@beginsWith {d}" "id:2001,deny,status:403"')

    return "\n".join(rules)

def save_modsec_rules(content):
    with open("modsecurity/dynamic_rules.conf", "w") as f:
        f.write(content)
