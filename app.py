from spider.crawl import CrawlProxy
from multiprocessing import Queue, Process

from config import PARSE_LIST

if __name__ == '__main__':
    result_q = Queue()
    html_content_q = Queue()
    crawl = CrawlProxy()
    process_list = []
    for parse in PARSE_LIST:
        p = Process(target=crawl.run, args=(parse, result_q, html_content_q))
        p.start()
        process_list.append(p)
    [p.join() for p in process_list]
    proxy_list = []
    while not result_q.empty():
        result = result_q.get()
        process_list += result
    print('process_list>>>', process_list)
