import chardet
import requests
from utils.request import get_headers


class HtmlDownload(object):
    def get_content(self, url):
        try:
            headers = get_headers()
            result = requests.get(url, headers=headers)
            if not result.ok:
                raise ConnectionError
            else:
                encoding = chardet.detect(result.content)['encoding']
                if encoding == 'Windows-1254':
                    result.encoding = 'utf8'
                else:
                    result.encoding = encoding
                return result.text
        except Exception as e:
            print('url: {} requests error \n error: {}'.format(url, e))
