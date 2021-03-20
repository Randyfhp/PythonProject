import json
import requests


class BaseRequest(object):

    def __init__(self):
        pass

    def get_url(self, app):
        return app

    def request_get(self, app, headers=None, params=None):
        return get(self.get_url(app), params, headers)

    def get(self, url, params=None, headers=None):
        with requests.request("GET", url, params=params, headers=headers) as res:
            print(params, headers, sep='\r\n')
            print(res.url, res.status_code)
            return self.get_json(res)

    def request_post(self, app, headers=None, params=None, data=None):
        if isinstance(data, dict):
            data = json.dumps(data)
        return self.post(self.get_url(app), params, headers, data)

    def post(self, url, params=None, headers=None, data=None):
        with requests.request("POST", url, params=params, headers=headers, data=data) as res:
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
        finally:
            return {}
