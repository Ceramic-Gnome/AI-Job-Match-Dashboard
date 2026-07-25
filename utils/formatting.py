from datetime import datetime, timedelta


def format_datetime(dt):
    if dt is None:
        return "N/A"

    return dt.strftime("%Y-%m-%d %H:%M:%S")


def get_job_badge(date_posted):

    if date_posted is None:
        return "Date Unknown", "gray"

    now = datetime.now()
    age = now - date_posted

    if age <= timedelta(days=1):
        return "New Today", "green"

    if age <= timedelta(days=7):
        return "This Week", "orange"

    return "Older", "gray"
