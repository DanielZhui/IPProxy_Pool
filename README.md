# IPProxy_Pool
> 单线程爬虫构建 IP 代理池

## 目录结构
``` shell
├── LICENSE
├── README.md
├── api # 将爬取经过验证的代理以 API 的形式对外提供服务
│   ├── __init__.py
│   └── web.py # 基于 Flask 构建简单 web
├── app.py  # 项目入口文件
├── config.py   # 配置文件
├── db_helper   # 数据库相关
│   ├── __init__.py
│   └── mongo_db.py # mongo 相关
├── spider  # 爬虫相关
│   ├── __init__.py
│   ├── crawl.py    # crawl engin
│   ├── html_downloader.py  # html downloader
│   └── html_parse.py   # html parser
└── utils   # utils
    ├── __init__.py
    ├── request.py  # request utils
    └── validator.py    # validate utils
```

## 如何使用
1. pip install -r ./requirement.txt
2. python app.py