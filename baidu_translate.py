# -*- coding: utf-8 -*-
import http.client
import hashlib
import urllib
import random
import json

def _get_password(path="E:\\Program_Files\\英译中朗读女\\password.txt"):
    with open(path) as f:
        lines = f.readlines()
    appid = lines[0].strip()
    secretKey = lines[1].strip()
    return appid,secretKey

def translateToChinese(q):
    appid, secretKey = _get_password()

    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'  # 原文语种
    toLang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    # q= "What's the simplest way of detecting keyboard input in python from the terminal?"
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        out = result['trans_result'][0]['dst']
        return out

    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
