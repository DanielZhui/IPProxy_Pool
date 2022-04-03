import time


def format_time(timestamp):
    local_time = time.localtime(timestamp / 1000)
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return date_time
