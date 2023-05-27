def is_within_time_window(new_message_timestamp, saved_message_timestamp, time_window_ms):
    time_diff = new_message_timestamp - saved_message_timestamp
    return time_diff <= time_window_ms

def format_latitude_longitude(value):
    if isinstance(value, float):
        return f'{value:.5f}'
    return value