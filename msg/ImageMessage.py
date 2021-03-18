from msg.BaseMessage import BaseMessage


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

    def set_image(self, image):
        self.image['base64'] = image

    def set_md5(self, md5):
        self.image['md5'] = md5
