def format_datetime(dt):
    if dt is None:
        return "N/A"

    return dt.strftime("%Y-%m-%d %H:%M:%S")