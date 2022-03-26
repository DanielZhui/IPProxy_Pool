import requests
from time import time
import config
from utils.request import get_headers


def check_proxy_list(proxy_list):
    validated_proxy_list = []
    for proxy in proxy_list:
        result, speed, verify_time = _check_proxy(proxy)
        if not result:
            continue
        proxy['speed'] = '{}ms'.format(speed)
        proxy['verify_time'] = verify_time
        validated_proxy_list.append(proxy)
    return validated_proxy_list


def _check_proxy(proxy):
    ip, port, type = proxy.get('ip'), proxy.get('port'), proxy.get('http')
    proxy = {}
    proxy[type] = '{}:{}'.format(ip, port)
    test_url = config.TEST_URL
    try:
        start_time = int(time() * 1000)
        headers = get_headers()
        res = requests.get(test_url, headers=headers, proxies=proxy)
        verify_time = int(time() * 1000)
        if res.ok:
            speed = int(time() * 1000) - start_time
            return True, speed, verify_time
        else:
            return False, 0, 0
    except Exception as e:
        print('IP: {} Port: {} error: {}'.format(ip, port, e))
        return False, 0, 0
