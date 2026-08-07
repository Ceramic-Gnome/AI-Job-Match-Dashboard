from datetime import datetime, timedelta


def format_datetime(dt):
    if dt is None:
        return "N/A"

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_job_badge(date_posted):

    if date_posted is None:
        return "Date Unknown", "gray"

    now = datetime.now().astimezone()
    age = now - date_posted

    if age <= timedelta(days=1):
        return "New Today", "green"

    if age <= timedelta(days=7):
        return "This Week", "orange"

    return "Older", "gray"


def get_match_color(score: float) -> str:
    if score >= 80:
        return "green"
    elif score >= 60:
        return "orange"
    return "red"
