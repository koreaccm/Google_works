import httplib
import urllib

httplib.HTTPConnection.debuglevel = 1
url = 'http://search.naver.com/search.naver?query=%ED%95%9C%EC%98%88%EC%8A%AC'
res = urllib.urlopen(url)
print res.read()

