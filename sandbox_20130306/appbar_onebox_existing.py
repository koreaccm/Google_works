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

import re
#import time

for row_index in range(sheet0.nrows):

#    time.sleep(0.7)
    keyword = sheet0.cell(row_index,0).value
    params = {'q' : keyword, 'hl' : 'ko'}
    enc_params = urllib.urlencode(params)
    
    request = urllib2.Request('http://sky-kpkr.sandbox.google.com/'+'search'+'?'+enc_params)
    request.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)
         
    onebox = soup.find_all(class_="g ssr noknav")
    #q="은교"의 경우, onebox가 SRP 하단에 위치함.
    appbar = soup.find_all(class_="appcenter")
    #class 값은 appcenter 외에도 몇 가지 더 존재함 
    
    
    if appbar:
        print "appbar"       
               
    elif onebox:
        print "onebox"
            
    else: 
        #nobox
        print "0"
        
    
    

    
    
   
