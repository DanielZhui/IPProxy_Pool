from app import start


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': start,
            # 每天凌晨执行爬虫任务
            'trigger': 'cron',
            'hour': 0,
            'minute': 0
        }
    ]

    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    ENV = 'development'
    # 如果 debug 模式开启会导致定时任务执行两次
    DEBUG = True
