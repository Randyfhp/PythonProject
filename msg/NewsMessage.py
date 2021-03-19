from msg.BaseMessage import BaseMessage


class NewsMessage(BaseMessage):
    MESSAGE_TYPE = 'news'

    def __init__(self):
        super(NewsMessage, self).__init__(self.MESSAGE_TYPE)
        self.article_list = []
        self.news = {
            'articles': self.article_list
        }

    def __dict__(self):
        obj = super(NewsMessage, self).__dict__()
        obj[self.MESSAGE_TYPE] = self.news
        return obj

    @classmethod
    def construct_article(cls, title, description, url, pic_url):
        article = {
            "title": title,
            "description": description,
            "url": url,
            "picurl": pic_url
        }
        return article

    def add_article(self, title, description, url, pic_url):
        article = self.construct_article(title, description, url, pic_url)
        self.article_list.append(article)

    def append_articles(self, articles):
        self.article_list.extend(articles)

    def set_articles(self, articles):
        self.article_list.clear()
        self.append_articles(articles)


