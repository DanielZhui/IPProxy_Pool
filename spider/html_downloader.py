import chardet
import requests
from utils.request import get_headers


class HtmlDownload(object):
    @staticmethod
    def get_content(self, url):
        try:
            headers = get_headers()
            result = requests.get(url, headers=headers)
            if not result.ok:
                raise ConnectionError
            if result.ok:
                result.encoding = chardet.detect(result.content)['encoding']
                return result.text
        except Exception as e:
            print('url: {} requests error \n error: {}'.format(url, e))
