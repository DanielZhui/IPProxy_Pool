from lxml import etree
from config import ParseType


class HtmlParse(object):
    def parse(self, content, parse):
        if parse['type'] == ParseType.IP.value:
            return self.parse_66ip(content, parse)
        if parse['type'] == ParseType.HIDE.value:
            return self.parse_hide(content, parse)
        if parse['type'] == ParseType.KUAI_DAI_LI.value:
            return self.parse_fast(content, parse)

    def base_parse(self, content, parse):
        html = etree.HTML(content)
        elms = html.xpath(parse['pattern'])
        return elms

    def get_proxy_list(self, parse, elms):
        proxy_list = []
        for e in elms:
            try:
                ip = e.xpath(parse['position'].get('ip'))[0].text
                port = e.xpath(parse['position'].get('port'))[0].text
                city = e.xpath(parse['position'].get('city'))[0].text
                type = e.xpath(parse['position'].get('type'))[0].text
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
        elms = self.base_parse(content, parse)
        proxy_list = self.get_proxy_list(parse, elms)
        if len(proxy_list):
            return proxy_list

    def parse_hide(self, content, parse):
        elms = self.base_parse(content, parse)
        proxy_list = self.get_proxy_list(parse, elms)
        if len(proxy_list):
            return proxy_list

    def parse_fast(self, content, parse):
        elms = self.base_parse(content, parse)
        proxy_list = self.get_proxy_list(parse, elms)
        if len(proxy_list):
            return proxy_list
