import requests
from bs4 import BeautifulSoup

from crawler.bean.TopDataBean import TopDataBean


class BaiduTopManager(object):

    def __init__(self):
        self.top_result = []

    def get_top(self, count):
        with requests.get('http://top.baidu.com/buzz?b=1&fr=topindex') as res:
            soup = BeautifulSoup(res.content)
            # print(soup.prettify())
            # 获取前10名的新闻
            top_table = soup.table
            for item in top_table.find_all('tr'):
                if len(item.find_all('td', class_='first')) == 0:
                    continue
                title = item.find_all('td', class_='keyword', limit=1)[0]
                title = title.find_all('a', class_='list-title', limit=1)[0]
                index = item.find_all('td', class_='first', limit=1)[0].span.string
                self.top_result.append(TopDataBean(index, title.string, title['href']))
                # print(index, title.string, title['href'])
                if len(self.top_result) == count:
                    break
            for item in self.top_result:
                print(item)
        return self.top_result
