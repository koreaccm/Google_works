#-*- coding: utf-8 -*-
import urllib, urllib2
import StringIO, gzip
# to require bs4
from bs4 import BeautifulSoup
# to read xls file
from xlrd import open_workbook


xls = open_workbook('test2.xls')
sheet0 = xls.sheet_by_index(0)

#to write in xls file
from tempfile import TemporaryFile
from xlwt import Workbook
        
book = Workbook()
sheet1 = book.add_sheet('result 1') 

import re, time

for row_index in range(sheet0.nrows):

    time.sleep(0.5)
    keyword = sheet0.cell(row_index,0).value
    params = {'q' : keyword, 'hl' : 'ko', 'tbo' : 'd'}
    enc_params = urllib.urlencode(params)
    
    #검색결과 페이지에 우측 박스가 나오지 않는다. url parameter가 빠져서 그런 것으로 추정 중
    request = urllib2.Request('http://sky-kpkr2.sandbox.google.com/'+'search'+'?'+enc_params)
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)
    
  
    #attribute div class = "kno-ft kno-xs", table class = "kno-fs ts"
    
    #caution: probably, find_all mehtod can't ....
        
    desctag = soup.find_all(class_="kno-desc kno-fb-ctx")
    
    if desctag:
        desctag_a = desctag[0].a
        #case: 바이오니아, tag classs는 존재하지만 text는 없음
        if desctag_a:
            print "1"
        else:
            print "0"
    else:
        print "00"
    

    

    
    

    
    
   
