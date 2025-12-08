def health_bar(current_health, max_health, bar_length):
    filled_length = int(bar_length * current_health // max_health)
    bar = "#" * filled_length + "-" * (bar_length - filled_length)
    return f"[{bar}]"
