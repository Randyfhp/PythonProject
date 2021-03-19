import json
import requests


class BaseRequest(object):

    def __init__(self):
        pass

    def get_url(self, app):
        return app

    def request_get(self, app, header=None, params=None):
        with requests.request("GET", self.get_url(app), params=params, headers=header) as res:
            print(params, header)
            print(res.url, res.status_code)
            return self.get_json(res)

    def request_post(self, app, header=None, params=None, data=None):
        if isinstance(data, dict):
            data = json.dumps(data)
        with requests.request("POST", self.get_url(app), params=params, headers=header, data=data) as res:
            print(header, params, data)
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
