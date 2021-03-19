from wxWorkRobot.msg.BaseMessage import BaseMessage


class MarkDownMessage(BaseMessage):
    MESSAGE_TYPE = 'markdown'

    def __init__(self):
        super(MarkDownMessage, self).__init__(self.MESSAGE_TYPE)
        self.markdown = {
            'content': '',
        }

    def __dict__(self):
        obj = super(MarkDownMessage, self).__dict__()
        obj[self.MESSAGE_TYPE] = self.markdown
        return obj

    def set_markdown_content(self, content):
        self.markdown['content'] = content


# 风格基类
class MarDownBaseStyle(object):
    def __init__(self, text):
        self.text = text

    def get_text(self):
        return self.text

    def __str__(self):
        return self.get_text()


# 标题类型
class MarkDownTitleStyle(MarDownBaseStyle):
    def __init__(self, text, level):
        super(MarkDownTitleStyle, self).__init__(text)
        if level in range(1, 7):
            self.text = '{} {}'.format('#' * level, text)


# 字体加粗
class MarkDownBoldStyle(MarDownBaseStyle):
    def __init__(self, text):
        super(MarkDownBoldStyle, self).__init__(text)
        self.text = '**{}**'.format(self.text)


# 链接风格
class MarkDownLinkStyle(MarDownBaseStyle):
    def __init__(self, text, link):
        super(MarkDownLinkStyle, self).__init__(text)
        self.text = '[{}]({})'.format(self.text, link)


# 代码风格
class MarkDownCodeStyle(MarDownBaseStyle):
    def __init__(self, text):
        super(MarkDownCodeStyle, self).__init__(text)
        self.text = '`{}`'.format(self.text)


# 引用风格
class MarkDownReferenceStyle(MarDownBaseStyle):
    def __init__(self, text):
        super(MarkDownReferenceStyle, self).__init__(text)
        self.text = '\n> {}'.format(self.text)


# 字体颜色
class MarDownTextColorStyle(MarDownBaseStyle):
    GREEN = 'info'
    GRAY = 'comment'
    ORANGE_READ = 'warning'

    def __init__(self, text, color):
        super(MarDownTextColorStyle, self).__init__(text)
        self.text = '<font color=\"{}\">{}</font>'.format(color, self.text)
