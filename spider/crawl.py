import threading

from spider.html_downloader import HtmlDownload
from spider.html_parse import HtmlParse
from utils.request import get_self_ip
from utils.validator import check_proxy_list


class CrawlProxy(object):

    def run(self, parse, result_q, html_content_q):
        self.start_crawl(parse, html_content_q)
        self.get_proxy_list(parse, result_q, html_content_q)

    def get_proxy_list(self, parse, result_q, html_content_q):
        html_parse = HtmlParse()
        self_ip = get_self_ip()
        while not html_content_q.empty():
            content = html_content_q.get()
            proxy_list = html_parse.parse(content, parse)
            if proxy_list:
                validated_proxy_list = check_proxy_list(self_ip, proxy_list)
                if validated_proxy_list:
                    result_q.put(validated_proxy_list)

    def start_crawl(self, parse, html_content_q):
        html_downloader = HtmlDownload()
        urls = parse.get('urls')
        for url in urls:
            print('start crawl url>>>>', url)
            t = threading.Thread(target=html_downloader.get_content, args=(url, html_content_q))
            t.setDaemon(True)
            t.start()
            t.join()
