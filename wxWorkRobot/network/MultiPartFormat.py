from wxWorkRobot.util.HashUtil import HashUtil


class MultiPartFormat(object):

    def __init__(self, headers, data, boundary=HashUtil.get_md5_hex('MultiPartFormat'.encode('utf-8'))):
        self.headers = headers
        self.data = data
        self.boundary = self.get_boundary(headers, boundary)

    def format_str(self, headers, data, boundary=HashUtil.get_md5_hex('MultiPartFormat'.encode('utf-8'))):
        self.headers = headers
        self.data = data
        self.boundary = self.get_boundary(headers, boundary)

    @classmethod
    def get_boundary(cls, headers, boundary):
        result = boundary
        if not isinstance(headers, dict):
            return result
        for key in dict(headers).keys():
            if 'content-type' == str(key).lower():
                for text in str(headers.get(key)).split(';'):
                    if 'boundary' in text:
                        result = text.split('=')[-1]
        return result

    def format_str(self):
        start = '--{}\r\nContent-Disposition: form-data; '.format(self.boundary)
        join_str = '{}="{}";'
        join_value = '{}={};'
        end_str = '--{}--'.format(self.boundary)
        args_str = ''
        if not isinstance(self.data, dict):
            return args_str
        for key, value in self.data.items():
            if isinstance(value, str):
                args_str += join_str.format(key, value)
            else:
                args_str += join_value.format(key, value)
        args_str = args_str[0:-1] + '\r\n'
        args_str = start + args_str
        args_str = args_str + '{}\r\n' + end_str
        return args_str


# if __name__ == '__main__':
#     f = MultiPartFormat({"Content-Type": 'multipart/form-data; boundary={}'.format('abcd'),
#                      "Content-Length": len("field")}, {
#         "name": "media",
#         "filename": "filename",
#         "filelength": 6
#     })
#     print(f.format_str().format("Content-Type:{}".format("113")))
