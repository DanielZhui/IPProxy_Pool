from spider.crawl import CrawlProxy
from multiprocessing import Process, Queue, Pool

from config import PARSE_LIST

if __name__ == '__main__':
    p = Pool(processes=3)
    crawl = CrawlProxy()
    for parse in PARSE_LIST:
        p.apply_async(crawl.run, args=(parse, ))
    p.close()
    p.join()
