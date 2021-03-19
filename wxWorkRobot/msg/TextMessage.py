from wxWorkRobot.msg.BaseMessage import BaseMessage


class TextMessage(BaseMessage):
    MESSAGE_TYPE = 'text'

    def __init__(self):
        super(TextMessage, self).__init__(self.MESSAGE_TYPE)
        self.mentioned_list = []
        self.mentioned_mobile_list = []
        self.text = {
            'content': '',
            'mentioned_list': self.mentioned_list,
            'mentioned_mobile_list': self.mentioned_mobile_list
        }

    def __dict__(self):
        obj = super(TextMessage, self).__dict__()
        obj[self.MESSAGE_TYPE] = self.text
        return obj

    def set_text_content(self, content):
        self.text['content'] = content

    def set_mentioned_list(self, mentioned_list):
        self.mentioned_list.clear()
        self.mentioned_list.extend(mentioned_list)

    def add_mentioned_list(self, mentioned):
        self.mentioned_list.append(mentioned)

    def set_mentioned_mobile_list(self, mentioned_mobile_list):
        self.mentioned_mobile_list.clear()
        self.mentioned_mobile_list.extend(mentioned_mobile_list)

    def add_mentioned_mobile_list(self, mentioned_mobile):
        self.mentioned_mobile_list.append(mentioned_mobile)

