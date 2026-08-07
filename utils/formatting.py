from datetime import datetime, timedelta, timezone


def ensure_utc(dt):
    if dt is None:
        return None

    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)

    return dt.astimezone(timezone.utc)


def format_datetime(dt):
    if dt is None:
        return "N/A"

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_job_badge(date_posted):

    if date_posted is None:
        return "Date Unknown", "gray"

    date_posted = ensure_utc(date_posted)

    now = datetime.now(timezone.utc)

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
