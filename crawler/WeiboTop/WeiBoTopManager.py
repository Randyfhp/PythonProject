import requests
from bs4 import BeautifulSoup

from crawler.bean.TopDataBean import TopDataBean


class WeiBoTopManager(object):

    def __init__(self):
        self.top_result = []

    def get_top(self, count):
        with requests.get('https://s.weibo.com/top/summary?cate=realtimehot') as res:
            soup = BeautifulSoup(res.content)
            # print(soup.prettify())
            top_table = soup.table.tbody
            # print(top_table)
            for item in top_table.find_all('tr'):
                content = item.find_all('td', class_='td-02', limit=1)[0].a
                indexElement = item.find_all('td', class_='td-01 ranktop', limit=1)
                if len(indexElement) == 0:
                    indexElement = item.find_all('td', class_='td-01', limit=1)
                    if len(indexElement) != 0:
                        index = '置顶'
                    else:
                        continue
                else:
                    index = indexElement[0].string
                address = 'https://s.weibo.com' + content['href']
                self.top_result.append(TopDataBean(index, content.string, address))
                # print(index, content.string, address)
                if len(self.top_result) == count:
                    break
            for item in self.top_result:
                print(item)
        return self.top_result
