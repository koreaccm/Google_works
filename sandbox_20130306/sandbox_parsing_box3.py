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
          
    sandbox1 = soup.find_all(class_="kno-ec rhsvw vk_rhsc kno-ec-si")
    sandbox2 = soup.find_all(class_="kno-ec rhsvw vk_rhsc")
    minibox = soup.find_all(class_="kno-sh")
    #class = "kno-sh ellip" : 함께 찾은 검색어도 minibox에 들어가버림
    topbox = soup.find_all(class_="g ssr noknav")
    #q="은교"의 경우, onebox가 SRP 하단에 위치함.
    appbar = soup.find_all(class_="appcenter")
    #class 값은 appcenter 외에도 몇 가지 더 존재함 
    
    if sandbox1 or sandbox2:
        print "1"
        
    elif minibox:
        minibox_str = minibox[0].string.encode("utf-8")
        text = "이것을 찾으셨나요?"
        minibox_str2 = text.encode("utf-8")
        
        if (minibox_str == minibox_str2):
        #minibox_first = soup.find_all(class_="kno-mcl rhsvw vk_rhsc")
        #m_url = minibox_first[0].a['href'].encode('utf-8')  
            print "2"
        
        else:
            print "what"
                
    elif topbox:
        print "3"
            
    elif appbar:
        print "4"
     
    else: 
        #nobox
        print "0"
        
    
    

    
    
   
