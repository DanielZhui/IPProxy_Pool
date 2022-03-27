import json
import requests
from random import choice
from config import USER_AGENTS, HTTPS_TEST_IP, REQUEST_TIME_OUT


def get_headers():
    return {
        'User-Agent': choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }


def get_self_ip():
    res = requests.get(HTTPS_TEST_IP, headers=get_headers(), timeout=REQUEST_TIME_OUT)
    if not res.ok:
        return
    res = json.loads(res.text)
    return res.get('origin')
