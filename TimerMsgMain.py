import sys

from crawler.WeiboTop.WeiBoTopManager import WeiBoTopManager
from crawler.bean.TopDataBean import TopDataBean
from crawler.BaiduTop.BaiduTopManager import BaiduTopManager
from wxWorkRobot.msg.MarkDownMessage import MarkDownMessage, MarDownTextColorStyle, MarkDownLinkStyle, MarkDownBoldStyle
from wxWorkRobot.network.RequestManager import RequestManager


def config_a_markdown_message(title, info):
    msg = MarkDownMessage()
    msg_text = str(MarDownTextColorStyle(str(MarkDownBoldStyle('{}热搜榜Top10\n'.format(title))),
                                         MarDownTextColorStyle.ORANGE_READ)) + \
               str(MarDownTextColorStyle('（每小时更新）\n', MarDownTextColorStyle.GRAY))
    for item in info:
        if not isinstance(item, TopDataBean):
            continue
        msg_text += str(MarkDownLinkStyle('{}.{}\n'.format(item.get_index(), item.get_title()), item.get_url()))
    msg.set_markdown_content(msg_text)
    return msg


def main(argc, argv):
    init()
    request_manager = RequestManager()
    baidu_manager = BaiduTopManager()
    weibo_manager = WeiBoTopManager()
    msg_baidu = config_a_markdown_message('百度', baidu_manager.get_top(10))
    msg_weibo = config_a_markdown_message('微博', weibo_manager.get_top(10))
    # print(msg_weibo.__dict__())
    request_manager.post_json(msg_baidu.__dict__())
    request_manager.post_json(msg_weibo.__dict__())


def init():
    RequestManager.init_config(
        'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=db34665b-6227-45ee-92c3-a17f47f38a57')


if __name__ == '__main__':
    init()
    main(len(sys.argv), sys.argv)
