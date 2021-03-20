import json
import requests


class BaseRequest(object):

    def __init__(self):
        pass

    def get_url(self, app):
        return app

    def request_get(self, app, header=None, params=None):
        return self.get(self.get_url(app), header, params)

    def get(self, url, header=None, params=None):
        with requests.request("GET", self.get_url(app), params=params, headers=header) as res:
            print(params, header, sep='\r\n')
            print(res.url, res.status_code)
            return self.get_json(res)

    def request_post(self, app, headers=None, params=None, data=None, **kwargs):
        if isinstance(data, dict):
            data = json.dumps(data)
        return self.post(self.get_url(app), headers, params, data, **kwargs)

    def post(self, url, headers=None, params=None, data=None, **kwargs):
        with requests.request("POST", url, params=params, headers=headers, data=data, **kwargs) as res:
            print(headers, params, data, sep='\r\n')
            print(res.url, res.status_code)
            return self.get_json(res)

    @classmethod
    def get_json(cls, res):
        try:
            print(res.content)
            return res.json()
        except Exception as e:
            print(e.args)
            return {}
