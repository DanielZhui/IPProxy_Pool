from time import sleep

import config
from spider.html_downloader import HtmlDownload
from spider.html_parse import HtmlParse
from db_helper.mongo_db import MongoHelper
from utils.request import get_self_ip
from utils.validator import check_proxy_list


class CrawlProxy(object):

    def run(self):
        result = []
        parse_list = config.PARSE_LIST
        for parse in parse_list:
            proxy_list = self.start_crawl(parse)
            self_ip = get_self_ip()
            validated_proxy_list = check_proxy_list(self_ip, proxy_list)
            result = result + validated_proxy_list
        sql_helper = MongoHelper()
        sql_helper.insert_many(result)
        return result

    def start_crawl(self, parse):
        proxy_info_list = []
        html_parse = HtmlParse()
        html_downloader = HtmlDownload()
        urls = parse.get('urls')
        for url in urls:
            print('start crawl url>>>>', url)
            # 手动加一个延迟，防止被服务器屏蔽
            sleep(3)
            content = html_downloader.get_content(url)
            if not content:
                continue
            proxy_list = html_parse.parse(content, parse)
            if not proxy_list:
                continue
            proxy_info_list = proxy_info_list + proxy_list
        return proxy_info_list
