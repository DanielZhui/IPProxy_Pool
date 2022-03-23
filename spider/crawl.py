from time import sleep
import gevent
from gevent.pool import Pool

from config import GEVENT_POOL
from spider.html_downloader import HtmlDownload
from spider.html_parse import HtmlParse


class CrawlProxy(object):
    def __int__(self):
        self.g_pool = Pool(GEVENT_POOL)

    def start_crawl(self, parse):
        html_parse = HtmlParse()
        html_downloader = HtmlDownload()
        urls = parse.get('urls')
        for url in urls:
            # 手动加一个延迟，防止被服务器屏蔽
            sleep(3)
            content = html_downloader.get_content(url)
            if not content:
                continue
            proxy_list = html_parse.parse(content, parse)
            print(proxy_list)
            if not proxy_list:
                continue
