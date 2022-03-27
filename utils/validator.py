import json
import requests
from time import time
import config
from utils.request import get_headers


def check_proxy_list(self_ip, proxy_list):
    validated_proxy_list = []
    for p in proxy_list:
        ip, port, city, type = p.get('ip'), p.get('port'), p.get('city'), p.get('type')
        proxy = {'http': '{}:{}'.format(ip, port), 'https': '{}:{}'.format(ip, port)}
        http, http_speed, http_verify_time = _check_proxy(self_ip, proxy)
        https, https_speed, https_verify_time = _check_proxy(self_ip, proxy, False)
        if not http and not https:
            continue
        if http:
            protocol = 'http'
            speed = http_speed
            verify_time = http_verify_time
        else:
            protocol = 'https'
            speed = https_speed
            verify_time = https_verify_time
        result = {
            'ip': ip,
            'port': port,
            'city': city,
            'type': type,
            'protocol': protocol,
            'speed': '{}ms'.format(speed),
            'verify_time': verify_time
        }
        validated_proxy_list.append(result)
    return validated_proxy_list


def _check_proxy(self_ip, proxy, http=True):
    if http:
        test_url = config.HTTP_TEST_IP
    else:
        test_url = config.HTTPS_TEST_IP
    try:
        start_time = int(time() * 1000)
        headers = get_headers()
        res = requests.get(test_url, headers=headers, proxies=proxy, timeout=config.REQUEST_TIME_OUT)
        verify_time = int(time() * 1000)
        if res.ok:
            origin = json.loads(res.text).get('origin')
            if origin and origin == self_ip:
                return False, 0, 0
            speed = int(time() * 1000) - start_time
            return True, speed, verify_time
        else:
            return False, 0, 0
    except Exception as e:
        print('proxy: {} test error: {}'.format(proxy, e))
        return False, 0, 0
