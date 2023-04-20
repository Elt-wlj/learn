# import os
# pid = os.fork()
# if pid == 0:
#     print('child %s parent %s' %(os.getpid(),os.getpid()))
# else:
#     print('its just child %s'%os.getpid())
from html.parser import HTMLParser
from urllib.request import Request, urlopen
import re


def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
    req = Request(url, headers=headers)
    with urlopen(req, timeout=25) as f:
        data = f.read()
        print(f'Status:{f.status} {f.reason}')
    return data.decode('utf-8')


class MyHtmlParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.__parsedata = ''
        self.info = []

    def handle_starttag(self, tag, attrs):

        if ('class', 'event-title') in attrs:
            self.__parsedata = 'name'
        if tag == 'time':
            self.__parsedata = 'time'
        if ('class', 'say-no-more') in attrs:
            self.__parsedata = 'year'
        if ('class', 'event-location' )in attrs:
            self.__parsedata = 'location'

    def handle_endtag(self, tag):
        self.__parsedata = ''

    def handle_data(self, data):

        if self.__parsedata == 'name':
            self.info.append('会议title：{}'.format(data))
        if self.__parsedata == 'time':
            self.info.append('会议time：{}'.format(data))
        if self.__parsedata == 'year':
            if re.match(r'\s\d{4}', data):
                self.info.append('会议year:{}'.format(data.strip()))
        if self.__parsedata == 'location':
            self.info.append('会议locate:{}'.format(data) +'\n')


def main():
    parser = MyHtmlParser()
    url = 'https://www.python.org/events/python-events/'
    data = get_data(url)
    parser.feed(data)
    for s in parser.info:
        print(s)


if __name__ == '__main__':
    main()
