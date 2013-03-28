#-*- coding: utf-8 -*-
import urllib, urllib2
import StringIO, gzip
# to require bs4
from bs4 import BeautifulSoup
# to read xls file
from xlrd import open_workbook


xls = open_workbook('test.xls')
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
    #user-agent 모바일로 변경
    request.add_header('User-agent', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; SHW-M250S Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)
          
    sandbox = soup.find_all(class_="kno-result")      
    #class = "kno-sh ellip" : 함께 찾은 검색어도 minibox에 들어가버림
    onebox = soup.find_all(class_="g ssr noknav")
    #q="은교"의 경우, onebox가 SRP 하단에 위치함.
    topstuff = soup.find_all("#topstuff")
    
    
    
    # sandbox & onebox, 또는 onebox & topstuff, 또는 topstuff & sandbox, 또는 sandbox & onebox & topstuff 일 경우에 모두 박스 종류값을 리턴해줘야한다.
    # 고민 중
    
    if sandbox:
        sheet1.write(row_index, 1, "kp"+len(sandbox))
    elif onebox:
        sheet1.write(row_index, 1, "srs"+len(onebox))
    elif topstuff:
        sheet1.write(row_index, 1, "srs"+len(onebox))

            
    else: 
        #nobox
        sheet1.write(row_index, 1, "0")

        
book.save('google_result.xls')    
    

    
    
   
