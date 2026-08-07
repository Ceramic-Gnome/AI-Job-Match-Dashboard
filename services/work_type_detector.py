def determine_work_type(description):

    text = (description or "").lower()

    if "remote" in text:
        return "Remote"

    if "hybrid" in text:
        return "Hybrid"

    if "on-site" in text or "onsite" in text:
        return "On-site"

    return "Unknown"
