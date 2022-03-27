from time import sleep
import chardet
import requests
from utils.request import get_headers


class HtmlDownload(object):
    def get_content(self, url, html_content_q):
        try:
            headers = get_headers()
            # 手动加一个延迟，防止被服务器屏蔽
            sleep(1)
            result = requests.get(url, headers=headers)
            if not result.ok:
                raise ConnectionError
            else:
                encoding = chardet.detect(result.content)['encoding']
                if encoding == 'Windows-1254':
                    result.encoding = 'utf8'
                else:
                    result.encoding = encoding
                html_content_q.put(result.text)
        except Exception as e:
            print('url: {} requests error \n error: {}'.format(url, e))
