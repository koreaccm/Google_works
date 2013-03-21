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
    params = {'query' : keyword}
    enc_params = urllib.urlencode(params)
    
    request = urllib2.Request('http://m.search.naver.com/'+'search'+'.'+'?'+enc_params)
    #user-agent 모바일로 변경
    request.add_header('User-agent', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; SHW-M250S Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)
          
    sandbox = soup.find_all(class_="")      
    onebox = soup.find_all(class_="g ssr noknav")


    
    
    if sandbox:
        sheet1.write(row_index, 1, "kp"+len(sandbox))  
            
    else: 
        sheet1.write(row_index, 1, "0")

        
book.save('naver_result.xls')    
    

    
    
   
