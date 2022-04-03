import time
from web.app import app


@app.template_filter("format_time")
def format_time(timestamp):
    local_time = time.localtime(timestamp / 1000)
    date_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return date_time
