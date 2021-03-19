from wxWorkRobot.msg.BaseMessage import BaseMessage


class FileMessage(BaseMessage):
    MESSAGE_TYPE = 'file'

    def __init__(self):
        super(FileMessage, self).__init__(self.MESSAGE_TYPE)
        self.file = {
            'media_id': ''
        }

    def __dict__(self):
        obj = super(FileMessage, self).__dict__()
        obj[self.MESSAGE_TYPE] = self.file
        return obj

    def set_file_id(self, str_id):
        self.file['media_id'] = str_id
