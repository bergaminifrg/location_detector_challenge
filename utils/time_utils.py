import datetime

def is_within_time_window(timestamp, time_window_minutes = 30):
    current_time = datetime.datetime.now()
    message_time = datetime.datetime.fromtimestamp(timestamp)
    time_diff = current_time - message_time
    time_diff_minutes = time_diff.total_seconds() / 60.0
    return time_diff_minutes <= time_window_minutes