__author__ = 'SWarren'
from urllib.parse import urlparse

class Urlsplit:
    def SplitIntoList(self,address):
        o = urlparse(address)
        if o.scheme or o.netloc != '':
            urlList = [o.scheme,o.netloc,o.path,o.query]
            return urlList
        else:
            return 'error in input'

'''print('%s' % Urlsplit().SplitIntoList('http://www.makeit.org/demo/appl?input=3'))

print('%s' % Urlsplit().SplitIntoList('http://.iloveyou.com/whatsup/hey.php?chicken=1'))'''


