
def detect_outdated_js(js_links):
    signatures = ["jquery-1.", "angular-1.", "bootstrap-2.", "vue-1."]
    return [js for js in js_links if any(sig in js for sig in signatures)]
