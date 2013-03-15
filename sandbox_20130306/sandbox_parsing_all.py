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
sheet1 = book.add_sheet('result 1', cell_overwrite_ok=True) 

import re
#import time

for row_index in range(sheet0.nrows):

#    time.sleep(0.7)
    keyword = sheet0.cell(row_index,0).value
    params = {'q' : keyword, 'hl' : 'ko'}
    enc_params = urllib.urlencode(params)
    
    request = urllib2.Request('http://www.google.co.kr/'+'search'+'?'+enc_params)
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
    desctag = soup.find_all(class_="kno-desc kno-fb-ctx")
    
    
    if sandbox1 or sandbox2:
        sheet1.write(row_index, 1, "sandbox")
        
        if desctag:
            desctag_a = desctag[0].a
            #case: 바이오니아, tag classs는 존재하지만 text는 없음
            if desctag_a:
                sheet1.write(row_index, 2,  "desc_y")
            else:
                sheet1.write(row_index, 2,  "desc_n")
            
    elif minibox:
        minibox_str = minibox[0].string.encode("utf-8")
        text = "이것을 찾으셨나요?"
        minibox_str2 = text.encode("utf-8")
        
        if (minibox_str == minibox_str2):
        #minibox_first = soup.find_all(class_="kno-mcl rhsvw vk_rhsc")
        #m_url = minibox_first[0].a['href'].encode('utf-8')  
            sheet1.write(row_index, 1, "minibox")
        
        else:
            sheet1.write(row_index, 1, "what")
                
    elif topbox:
        sheet1.write(row_index, 1, "onebox")
            
    else: 
        #nobox
        sheet1.write(row_index, 1, "no box")

        
book.save('result.xls')    
    

    
    
   
