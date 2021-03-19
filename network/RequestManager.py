import json
from urllib import parse
import requests

from util import FileUtil


class RequestManager(object):
    BASE_URL = ""
    BASE_KEY = ""
    BASE_APP = {
        'send': "cgi-bin/webhook/send",
        'upload_media': "webhook/upload_media"
    }

    @classmethod
    def init_config(cls, webhook_url):
        # url 解码
        url_data = parse.unquote(webhook_url)
        # 解析url
        parse_result = parse.urlparse(url_data)
        # 获取查询的参数
        query = parse.parse_qs(parse_result.query)
        # 获取base url
        cls.BASE_URL = parse.urlunsplit((parse_result.scheme, parse_result.netloc, '', '', ''))
        # 获取key
        cls.BASE_KEY = query.get('key', [])

    def get_url(self, app):
        return parse.urljoin(self.BASE_URL, self.BASE_APP.get(app, ''))

    def request_get(self, params, header, app):
        with requests.request("GET", self.get_url(app), params=params, headers=header) as res:
            print(params, header)
            print(res.url, res.status_code)
            return res.content

    def request_post(self, params, header, app, data):
        with requests.request("POST", self.get_url(app), params=params, headers=header, data=json.dumps(data)) as res:
            print(res.url, res.status_code)
            print(data, header)
            return res.content

    def post_json(self, data):
        header = {"Content-Type": 'application/json'}
        result = self.request_post(None, header, 'send', data)

    def upload_file(self, file_path):
        header = {
            "Content-Type": """multipart/form-data';
                                boundary=-------------------------acebdf13572468
                                Content-Length: 220
                                ---------------------------acebdf13572468
                                Content-Disposition: form-data; name="media";filename="{}"; filelength={}
                                Content-Type: application/octet-stream
                                mytext
                                ---------------------------acebdf13572468--
            """.format(file_path, FileUtil.get_file_size(file_path))
        }
        query = {
            'key': self.BASE_KEY,
            'type': 'file'
        }
        result = self.request_post(query, header, 'upload_media', None)
        print(result)
        return result['media_id']
