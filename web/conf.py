from app import start


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': start,
            'trigger': 'interval',
            'seconds': 600
        }
    ]

    SCHEDULER_API_ENABLED = True
    ENV = 'development'
    # 如果 debug 模式开启会导致定时任务执行两次
    DEBUG = False
