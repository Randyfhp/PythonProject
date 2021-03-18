import json

import requests


class RequestManager(object):
    BASE_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=db34665b-6227-45ee-92c3-a17f47f38a57"

    def get_base_url(self):
        return self.BASE_URL

    def request_get(self, params, header):
        with requests.request("GET", self.get_base_url(), params=params, headers=header) as res:
            print(params, header)
            print(res.url, res.status_code)
            return res.content

    def request_post(self, params, header):
        with requests.request("POST", self.get_base_url(), headers=header, data=json.dumps(params)) as res:
            print(res.url, res.status_code)
            print(params, header)
            return res.content

    def post_json(self, params):
        header = {"Content-Type": 'application/json'}
        result = self.request_post(params, header)
