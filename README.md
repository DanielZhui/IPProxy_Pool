# IPProxy_Pool
> 🚀 Building Ip Proxy Pool

## Project Structure
``` shell
├── LICENSE
├── Makefile        # make 服务启动命令
├── README.md
├── app.py          # crawl 启动入口
├── config.py       # crawl config
├── data            # docker mongo data
├── db_helper       # db
│   ├── __init__.py
│   └── mongo_db.py
├── dev.dockerfile.yml  # dev docker-compose file
├── dockerfile
├── requirements.txt
├── spider              # spider
│   ├── __init__.py
│   ├── crawl.py
│   ├── html_downloader.py  # html downloader
│   └── html_parse.py       # html parse
├── utils               # crawl utils
│   ├── __init__.py
│   ├── request.py
│   └── validator.py
└── web                 # use flask to provide web service
    ├── __init__.py
    ├── app.py
    ├── conf.py
    ├── tem_filters
    │   └── timer.py
    ├── templates
    │   └── index.html
    └── util.py
```

## How to start
> 该项目提供两种启动方式
1. docker 容器启动
    1. 在项目根目录下执行：make start-dev

2. 本机启动
   1. pip install -r ./requirement.txt
   2. cd web && python app.py【启动 web 服务同时开启爬虫定时任务】
      - 如果仅想启动爬虫可以在项目根目录使用：python app.py

## Feature
1. 提供 web proxy html
   - http://159.75.80.164:50000/home
2. 提供开放 API 开放调用，获取有效代理服务列表
   - http://159.75.80.164:50000/api/proxys
3. 项目会在每天晚上 12:00 更新代理

## 爬取数据源
- [快代理](https://www.kuaidaili.com/free/)
- [66代理](http://www.66ip.cn/index.html)


## demo
1. [web proxy html](http://159.75.80.164:50000/home)
2. [Open API](http://159.75.80.164:50000/api/proxys)

## Tips:
> 欢迎大家提供更多数据源地址