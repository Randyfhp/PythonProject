import sys

from wxWorkRobot.msg.TextMessage import TextMessage
from wxWorkRobot.msg.MarkDownMessage import *
from wxWorkRobot.msg.ImageMessage import ImageMessage
from wxWorkRobot.msg.NewsMessage import NewsMessage
from wxWorkRobot.msg.FileMessage import FileMessage
from wxWorkRobot.network.RequestManager import RequestManager


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


def config_a_image_message(manager):
    msg = ImageMessage()
    msg.set_image('./src/image_message_test.jpeg')
    return msg


def config_a_news_message():
    msg = NewsMessage()
    msg.add_article('中秋节礼品领取', '今年中秋节公司有豪礼相送', 'www.qq.com',
                    'http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png')
    return msg


def config_a_file_message(manager):
    msg = FileMessage()
    media_id = manager.upload_file3('./hello_world.txt')
    msg.set_file_id(media_id)
    return msg


def main(argc, argv):
    init()
    manager = RequestManager()
    msg = config_a_text_message()
    msg = config_a_markdown_message()
    msg = config_a_image_message(manager)
    # msg = config_a_news_message()
    # msg = config_a_file_message(manager)
    # print(msg.__dict__())
    manager.post_json(msg.__dict__())


def init():
    RequestManager.init_config(
        'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=db34665b-6227-45ee-92c3-a17f47f38a57')


# https://work.weixin.qq.com/api/doc/90000/90136/91770
if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
