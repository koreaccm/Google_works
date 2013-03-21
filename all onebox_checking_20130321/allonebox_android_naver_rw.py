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
    
    request = urllib2.Request('http://m.search.naver.com/'+'search.naver'+'?'+enc_params)
    #user-agent 모바일로 변경
    request.add_header('User-agent', 'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; SHW-M250S Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)
    
    # naver SRP tree는 <section> 순서. 단, "통합웹", "통합웹베스트"는 <div class="sc">
    # class에 csu 값이 포함된 것("cus*", "csu_xxx", "csu xxx")을 찾기 
    
    
    section=soup.find_all('section')
    #category=soup.find_all()
    section

"""    
    tv=soup.find_all(id='bdcast_area')
    #radio=
    movie=soup.find_all(class_='csu_hh cs_movieinfo ca')
    #theater=
    music=soup.find_all(id='music_top_id')
    people=soup.find_all(id='mcontent_people')
    #event=
    #sports=
    place=soup.find_all(class_='csu_hh cs_local')
    food=soup.find_all(id='dss_ingredient_body')
    #gov=
    #game=
    #country=
    school=soup.find_all(class_='csu3 cs_university')
    book=soup.find_all(class_='cs_nbook')
    term=soup.find_all(id='dic')
    company=soup.find_all(class_='ccsu_hh cs_finan')
    #hotel=
    mobile_app=soup.find_all(class_='csu_hh cs_appl')
    weather=soup.find_all(class_='csu_hh cs_weather')
    enc=soup.find_all(class_='li1 kdic')
    """
"""
    onebox=soup.find_all(class_="csu3")
    
    if tv in section[0]:
        print 'tv'
"""

"""    
    if sandbox:
        sheet1.write(row_index, 1, "kp"+len(sandbox))              
    else: 
        sheet1.write(row_index, 1, "0")
"""
        
#book.save('naver_result.xls')    
    

    
    
   
