#-*- coding: utf-8 -*-
import httplib, urllib, urllib2
import StringIO, gzip

httplib.HTTPConnection.debuglevel = 1
query_args = {'query':'house'}
encoded_args = 'search.naver?'+ urllib.urlencode(query_args)
print encoded_args

request = urllib2.Request('http://searchc.naver.com/')
request.add_header('User-agent', 'Mozilla/5.0')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request, encoded_args)

compressedstream = StringIO.StringIO(response.read())
gzipper = gzip.GzipFile(fileobj=compressedstream)

print gzipper.read().encode('utf-8')
