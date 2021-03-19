import hashlib


class HashUtil(object):

    @staticmethod
    def get_md5(all_byte):
        processor = HashUtil.get_processor('md5', all_byte)
        return processor.digest()

    @staticmethod
    def get_md5_hex(all_byte):
        processor = HashUtil.get_processor('md5', all_byte)
        return processor.hexdigest()

    @classmethod
    def get_processor(cls, hash_type, all_byte):
        lower_str = str(hash_type).lower()
        return hashlib.new(lower_str, all_byte)