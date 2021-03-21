class TopDataBean(object):
    def __init__(self, index, title, url):
        self.index = index
        self.title = title
        self.url = url
        
    def __str__(self):
        return '({},{},{})'.format(self.index, self.title, self.url)

    def get_index(self):
        return self.index

    def get_title(self):
        return self.title

    def get_url(self):
        return self.url
