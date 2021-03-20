import base64


class Base64Util(object):

    @staticmethod
    def encode_bytes(all_byte):
        return base64.b64encode(all_byte)

    @staticmethod
    def encode_str(string, encoding='utf-8'):
        all_byte = str(string).encode(encoding)
        return Base64Util.encode_bytes(all_byte)

    @staticmethod
    def decode_bytes(all_byte):
        return base64.decodebytes(all_byte)

    @staticmethod
    def decode_str(all_byte, decoding='utf-8'):
        return Base64Util.decode_bytes(all_byte).decode(decoding)


# if __name__ == '__main__':
#     encode = str('hello_world.txt').encode('utf-8')
#     print(encode)
#     print(Base64Util.encode_bytes(encode))
#     print(Base64Util.decode_str(Base64Util.encode_bytes(encode)))
