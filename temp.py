#-*- coding: utf-8 -*-
import urllib, urllib2
import StringIO, gzip
#to read xls file
        
params = {'q':'한예슬'}
enc_params = urllib.urlencode(params)
    
request = urllib2.Request('https://www.google.co.kr/'+'search'+'?'+enc_params)
request.add_header('User-agent', 'Mozilla/5.0')
request.add_header('Accept-encoding', 'gzip')
response = urllib2.urlopen(request)

compressedstream = StringIO.StringIO(response.read())
gzipper = gzip.GzipFile(fileobj=compressedstream)

data = gzipper.read().encode('utf-8') 
print data
