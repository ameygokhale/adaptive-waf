
import time

rate_cache = {}

def apply_rules(request, rules):
    path = request.path.lower()
    body = request.get_data(as_text=True).lower()
    ip = request.remote_addr or "unknown"

    for p in rules["restricted_paths"]:
        if path.startswith(p):
            return {"blocked": True, "reason": "Restricted path"}

    for keyword in rules["block_patterns"]:
        if keyword in path or keyword in body:
            return {"blocked": True, "reason": f"Pattern: {keyword}"}

    if "admin" in path and "admin" in rules["rate_limit"]:
        limit = rules["rate_limit"]["admin"]
        key = f"{ip}:{path}"
        now = time.time()

        rate_cache.setdefault(key, [])
        rate_cache[key] = [t for t in rate_cache[key] if now - t < 5]
        rate_cache[key].append(now)

        if len(rate_cache[key]) > limit:
            return {"blocked": True, "reason": "Rate limit exceeded"}

    return {"blocked": False, "reason": ""}
