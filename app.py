from config import PARSE_LIST
from spider.crawl import CrawlProxy


if __name__ == '__main__':
    crawl = CrawlProxy()
    for parse in PARSE_LIST:
        crawl.start_crawl(parse)
