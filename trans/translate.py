# coding=utf-8
import os
import sys
import time
import json
import http.client
import hashlib
import urllib
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import Global_config

"""
官方文档：https://fanyi-api.baidu.com/doc/21
"""


class Baidu_trans(object):
    def __init__(self):
        conf = Global_config()
        self.global_config = conf.global_config
        self.appid = str(self.global_config.get('baidu', '').get('appid', ''))
        self.secret_key = self.global_config.get('baidu', '').get('secret_key')
        self.from_lang = self.global_config.get('baidu', '').get('from_lang')
        self.to_lang = self.global_config.get('baidu', '').get('to_lang')

        """
        返回状态码2000为成功
                2001为错误
        """

    def get_url(self, query):
        base_url = '/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = self.appid + query + str(salt) + self.secret_key
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = base_url + '?appid=' + self.appid + '&q=' + urllib.parse.quote(
            query) + '&from=' + self.from_lang + '&to=' + self.to_lang + '&salt=' + str(
            salt) + '&sign=' + sign
        return myurl

    def get_url_to_lang(self, query, toLang):
        base_url = '/api/trans/vip/translate'
        salt = random.randint(32768, 65536)
        sign = self.appid + query + str(salt) + self.secret_key
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = base_url + '?appid=' + self.appid + '&q=' + urllib.parse.quote(
            query) + '&from=' + self.from_lang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        return myurl

    def trans(self, query):
        httpClient = None
        myurl = self.get_url(query)
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            data = result.get('trans_result', ['error'])[0]
            error_code = result.get('error_code', '')
            error_msg = result.get('error_msg', '')

            if isinstance(data, dict):
                code = 2000
            else:
                code = 2001
            return {"code": code, "result": data, "error_code": error_code, "error_msg": error_msg}
        except Exception as e:
            print(e)
            return {"code": 2001, "data": {}}

        finally:
            if httpClient:
                httpClient.close()

    def trans_to_lang(self, query, toLang):
        httpClient = None
        myurl = self.get_url_to_lang(query, toLang)
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            data = result.get('trans_result', ['error'])[0]
            error_code = result.get('error_code', '')
            error_msg = result.get('error_msg', '')

            if isinstance(data, dict):
                code = 2000
            else:
                code = 2001
            return {"code": code, "result": data, "error_code": error_code, "error_msg": error_msg}
        except Exception as e:
            print(e)
            return {"code": 2001, "data": {}}

        finally:
            if httpClient:
                httpClient.close()

    def trans_limit(self, query):
        result = self.trans(query)
        time.sleep(1.1)
        return result


#
if __name__ == '__main__':
    trans = Baidu_trans()
    query_list = [
        "返水计算方式-返水=用户的总投注*0.5%"
    ]

    for query in query_list:
        res = trans.trans(query)
        if res.get("code") == 2000:
            print(res["result"]["dst"])
        else:
            print("code:{}".format(res["code"]))
