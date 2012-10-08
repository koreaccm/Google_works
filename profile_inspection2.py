#-*- coding: utf-8 -*-
import httplib
httplib.HTTPConnection.debuglevel = 1

import urllib, urllib2
import StringIO, gzip
from xlrd import open_workbook

xls = open_workbook('test.xls')
sheet0 = xls.sheet_by_index(0)
for row_index in range(sheet0.nrows):
    #여기서 한글 인코딩 문제가 생
    keyword = sheet0.cell(row_index,0).value
    query_args = {'ie':'utf8','sm':'stp_hty','where':'se','query':keyword}
    encoded_args = 'search.naver?'+ urllib.urlencode(query_args)
    print encoded_args

    request = urllib2.Request('http://searchc.naver.com/')
    request.add_header('User-agent', 'Mozilla/5.0')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request, encoded_args)

    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read().encode('utf-8')
    
    if (data.find('section') == 1):
        print 'yes'
    else:
        print 'no'
        

    