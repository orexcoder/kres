import time
from random import randint

import requests
from anti_useragent import UserAgent as ua
from loguru import logger

import config

def get_headers(): return config.HEADERS.copy()

def setup_session(proxy: str):
    session = requests.Session()
    headers = get_headers()
    headers["User-Agent"] = ua().random
    session.headers = headers
    session.proxies.update({'https': 'http://' + proxy})
    return session

def subscribe_kresko(mail: str, proxy: str):
    time.sleep(randint(10, 15))
    email = mail.split(":")[0]

    session = setup_session(proxy)

    data = {
        "data": [{"email": email}]
    }

    resp = session.post(
        "https://www.kresko.fi/api/signup",
        data,
    )

    if resp.status_code == 200:
        logger.success(f" {email} successfully registered!")
        with open('files/registered.txt', 'a') as file:
            file.write(f'{proxy}:{mail}\n')
    else:
        logger.error(f" {email} - {resp.status_code}")


