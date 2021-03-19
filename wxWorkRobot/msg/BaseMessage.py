class BaseMessage(object):

    BASE_MESSAGE_TYPE = 'msgtype'

    def __init__(self, msg_type):
        self.msg_type = msg_type

    def get_type(self):
        return self.msg_type

    def set_type(self, msg_type):
        self.msg_type = msg_type

    def __dict__(self):
        return {
            self.BASE_MESSAGE_TYPE: self.msg_type
        }
