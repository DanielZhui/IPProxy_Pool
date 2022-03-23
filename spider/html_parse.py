from lxml import etree
from config import ParseType


class HtmlParse(object):
    def parse(self, content, parse):
        if parse['type'] == ParseType.IP:
            return self.parse_66ip(content, parse)
        if parse['type'] == ParseType.HIDE:
            return self.parse_hide(content, parse)
        if parse['type'] == ParseType.HIDE:
            return self.parse_fast(content, parse)

    def base_parse(self, content, parse):
        html = etree.html(content)
        elms = html.xpath(parse['pattern'])
        return elms

    def get_proxy_list(self, parse, elms):
        proxy_list = []
        for e in elms:
            try:
                ip = e.xpath(parse['position'].get('ip'))
                port = e.xpath(parse['position'].get('port'))
                city = e.xpath(parse['position'].get('city'))
                type = e.xpath(parse['position'].get('type'))
                proxy_list.append({
                    'ip': ip,
                    'port': port,
                    'city': city,
                    'type': type
                })
            except Exception as e:
                continue
        return proxy_list

    def parse_66ip(self, content, parse):
        elms = self.base_parse(content)
        proxy_list = self.get_proxy_list(parse, elms)
        if len(proxy_list):
            return proxy_list

    def parse_hide(self, content, parse):
        elms = self.base_parse(content)
        proxy_list = self.get_proxy_list(parse, elms)
        if len(proxy_list):
            return proxy_list

    def parse_fast(self, content, parse):
        elms = self.base_parse(content, parse)
        proxy_list = self.get_proxy_list(parse, elms)
        if len(proxy_list):
            return proxy_list
