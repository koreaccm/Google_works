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


except_cate = [u'바로가기',u'동영상',u'사이트',u'이미지',u'뉴스',u'오픈캐스트',u'매거진',u'지도',u'파워링크']

for row_index in range(sheet0.nrows):

#    time.sleep(0.7)
    keyword = sheet0.cell(row_index,0).value.encode('utf-8')
    params = {'query' : keyword, 'where':'m'}
    enc_params = urllib.urlencode(params)
    
    request = urllib2.Request('http://m.search.naver.com/'+'search.naver'+'?'+enc_params)
    #user-agent 모바일로 변경
    request.add_header('User-agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Galaxy Nexus Build/JRO03C) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)

    section = soup.find_all('section')
    
    h2_tag = [section[i].h2 for i in range(5, len(section))]
    h2_tag_cl = filter(None, h2_tag)


    j=0
    while j < len(h2_tag_cl):
        if h2_tag_cl[j] in except_cate:
            del h2_tag_cl[j]
        else:
            j+=1
    
    h2_str=[]
    for k in range(len(h2_tag_cl)):
        h2_str += [h2_tag_cl[k].get_text().encode('utf-8')]
    print h2_str                    



    
    # naver SRP tree는 <section> 순서. 단, "통합웹", "통합웹베스트"는 <div class="sc">
    # class에 csu 값이 포함된 것("cus*", "csu_xxx", "csu xxx")을 찾기 
    
