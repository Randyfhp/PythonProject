from wxWorkRobot.msg.BaseMessage import BaseMessage
from wxWorkRobot.util.Base64Util import Base64Util
from wxWorkRobot.util.HashUtil import HashUtil


class ImageMessage(BaseMessage):
    MESSAGE_TYPE = 'image'

    def __init__(self):
        super(ImageMessage, self).__init__(self.MESSAGE_TYPE)
        self.image = {
            'base64': '',
            'md5': '',
        }

    def __dict__(self):
        obj = super(ImageMessage, self).__dict__()
        obj[self.MESSAGE_TYPE] = self.image
        return obj

    def set_base64_image(self, base64_image):
        self.image['base64'] = base64_image

    def set_md5(self, md5):
        self.image['md5'] = md5

    def set_image(self, image):
        with open(image, 'rb') as file:
            image_byte = file.read()
            image_md = HashUtil.get_md5_hex(image_byte)
            self.set_md5(image_md)
            image_base64 = Base64Util.encode_bytes(image_byte)
            self.set_base64_image(image_base64)

