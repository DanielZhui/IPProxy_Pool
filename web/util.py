from time import time

ONE_DAY_MS = 24 * 60 * 60 * 1000


def get_find_options():
    current_time = int(time()*1000)
    # 获取小于当前时间2天的所有数据
    return {'verify_time': {'$gte': (current_time - 2 * ONE_DAY_MS)}}
