import sys

from msg.TextMessage import TextMessage
from msg.MarkDownMessage import *
from msg.ImageMessage import ImageMessage
from RequestManager import RequestManager


def config_a_text_message():
    msg = TextMessage()
    msg.set_text_content("这是用python发的")
    msg.add_mentioned_list('@all')
    return msg


def config_a_markdown_message():
    msg = MarkDownMessage()
    msg.set_markdown_content("实时新增用户反馈" +
                             str(MarDownTextColorStyle('132例', MarDownTextColorStyle.ORANGE_READ)) +
                             "请相关同事注意。\n" +
                             str(MarkDownReferenceStyle('类型:')) +
                             str(MarDownTextColorStyle('用户反馈\n', MarDownTextColorStyle.GRAY)) +
                             str(MarkDownReferenceStyle('普通用户反馈:')) +
                             str(MarDownTextColorStyle('117例\n', MarDownTextColorStyle.GRAY)) +
                             str(MarkDownReferenceStyle('VIP用户反馈:')) +
                             str(MarDownTextColorStyle('15例', MarDownTextColorStyle.GRAY)))
    return msg


def config_a_image_message():
    msg = ImageMessage()
    msg.set_image("image")
    msg.set_md5("md5 code")
    return msg


def main(argc, argv):
    msg = config_a_text_message()
    msg = config_a_markdown_message()
    msg = config_a_image_message()
    print(msg.__dict__())
    # RequestManager().post_json(msg.__dict__())


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
