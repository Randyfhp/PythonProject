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
            "Content-Type": FileUtil.get_file_content_type(file_path)
        }
        header = {
            "Content-Type": 'multipart/form-data; boundary={}'.format(self.get_split()),
            "Content-Length": 0
        }
        field = MultiPartFormat(header, request).format_str().format(
            """{}\n\r
            {}
            """.format(request['Content-Type'], data))
        header['Content-Length'] = str(len(field))
        params = {
            'key': self.BASE_KEY,
            'type': 'file'
        }
        result = self.request_post('upload_media', header, params, data=field)
        print(result)
        return result.get('media_id')
    
    # 直接上传文件
    def upload_file2(self, file_path):
        params = {
            'debug': 1,
            'key': self.BASE_KEY,
            'type': 'file'
        }
        with open(file_path, 'rb') as fd:
            file_byte = fd.read()
        files = {
            'file': (FileUtil.get_file_name(file_path),
                     file_byte,
                     FileUtil.get_file_content_type(file_path))
        }
        result = self.request_post('upload_media', None, params, data=None, files=files)
        return result['media_id']

    # 添加参数配置
    def upload_file3(self, file_path):
        """
            POST https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=693a91f6-7xxx-4bc4-97a0-0ec2sifa5aaa&type=file HTTP/1.1
            Content-Type: multipart/form-data; boundary=-------------------------acebdf13572468
            Content-Length: 220
            ---------------------------acebdf13572468
            Content-Disposition: form-data; name="media";filename="wework.txt"; filelength=6
            Content-Type: application/octet-stream
            mytext
            ---------------------------acebdf13572468--
        """
        params = {
            # 'debug': 1,
            'key': self.BASE_KEY,
            'type': 'file'
        }
        with open(file_path, 'rb') as fd:
            file_byte = fd.read()
        files = {
            'name': (None, 'media'),
            'filename': (None, FileUtil.get_file_name(file_path)),
            'filelength': (None, FileUtil.get_file_size(file_path)),
            'media': (FileUtil.get_file_name(file_path), file_byte, FileUtil.get_file_content_type(file_path))
        }
        result = self.request_post('upload_media', None, params, data=None, files=files)
        print(result)
        return result['media_id']
