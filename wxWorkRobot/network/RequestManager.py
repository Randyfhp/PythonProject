from urllib import parse

from wxWorkRobot.network.BaseRequest import BaseRequest
from wxWorkRobot.network.MultiPartFormat import MultiPartFormat
from wxWorkRobot.util import FileUtil
from wxWorkRobot.util.HashUtil import HashUtil


class RequestManager(BaseRequest):
    BASE_URL = ""
    BASE_KEY = ""
    BASE_APP = {
        'send': "cgi-bin/webhook/send",
        'upload_media': "cgi-bin/webhook/upload_media"
    }

    def __init__(self):
        super(RequestManager, self).__init__()

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

    def post_json(self, data):
        header = {"Content-Type": 'application/json'}
        result = self.request_post('send', header, data=data)
        return result

    @classmethod
    def get_split(cls):
        return HashUtil.get_md5_hex(cls.__name__.encode('utf-8'))

    def upload_file(self, file_path):
        data = None
        field = None
        with open(file_path, 'rb') as file:
            data = file.read()
        request = {
            "name": 'media',
            "filename": FileUtil.get_file_name(file_path),
            "filelength": FileUtil.get_file_size(file_path),
        }
        header = {
            "Content-Type": 'multipart/form-data; boundary={}'.format(self.get_split()),
            "Content-Length": 0
        }
        field = MultiPartFormat(header, request).format_str().format(
            '{}: {}\n\r\n\r{}'.format("Content-Type", FileUtil.get_file_content_type(file_path), data))
        header['Content-Length'] = str(len(field))
        params = {
            'debug': 1,
            'key': self.BASE_KEY,
            'type': 'file'
        }
        result = self.request_post('upload_media', header, params, data=field)
        print(result)
        return result.get('media_id')
#
#     def upload_test(self):
#         file = '../../hello_world.txt'
#         file_data = ''
#         with open(file, 'r') as fp:
#             file_data = fp.read()
#         field = """POST https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=db34665b-6227-45ee-92c3-a17f47f38a57&type=file HTTP/1.1
# 'Content-Type': 'multipart/form-data; boundary=00afab46c316c2a37e2ac90646d5c15f'
# 'Content-Length': 219
# --00afab46c316c2a37e2ac90646d5c15f
# Content-Disposition: form-data; name="media"; filename="hello_world.txt"; filelength={}
# Content-Type: application/octet-stream
#
# {}
# --00afab46c316c2a37e2ac90646d5c15f--""".format(len(file_data), file_data)
#
#         self.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=db34665b-6227-45ee-92c3-a17f47f38a57&type=file', data=field)
#
#
# if __name__ == '__main__':
#     RequestManager().upload_file('../../hello_world.txt')
