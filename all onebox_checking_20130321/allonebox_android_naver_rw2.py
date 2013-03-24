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
        
book = Workbook(encoding='utf-8')
sheet1 = book.add_sheet('result 1', cell_overwrite_ok=True) 

import re
import time
#import operator



except_cate = [u'바로가기',u'사이트',u'이미지',u'뉴스',u'오픈캐스트',u'매거진',u'지도',u'파워링크 ',u'통합웹베스트 미리보기뷰어',u'통합웹 미리보기뷰어',u'동영상',u'지식쇼핑']
direct_cate = u'바로가기'
people_cate = u'인물정보'


for row_index in range(sheet0.nrows):

    time.sleep(5)
    s_value = sheet0.cell(row_index,0).value
    if type(s_value) != unicode: s_value = str(s_value)
    
    keyword = s_value.encode('utf-8')
    params = {'query' : keyword, 'where':'m'}
    enc_params = urllib.urlencode(params)
    
    request = urllib2.Request('http://m.search.naver.com/'+'search.naver'+'?'+enc_params)
    #user-agent 모바일로 변경
    request.add_header('User-agent', 'Mozilla/5.0 (Linux; U; Android 2.3.5; ko-kr; SHW-M250S Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)
    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read()
    soup = BeautifulSoup(data)
    class_sc = soup.find_all(class_='sc')
    
    # find_all은 list type을 반환
    # 참고: soup.select('#id name') 또는 .select('.class name'), .findChildren(), from xml.dom import minidom(childNodes 개수와 직계 자손 이용하기 위함), .wrap/.unwrap
    
    h2_tag = {class_sc[i].h2 : i for i in range(len(class_sc)) if class_sc[i].h2 != None}

    #바로가기 있을 때 모든 rank 숫자를 하나 더 빼야함
    for (title,num) in h2_tag.items():
        title_txt = title.get_text()
        if title_txt == direct_cate:
            for (title,num) in h2_tag.items():
                h2_tag[title] = num - 1
        elif title_txt == people_cate:
            # 인물정보 있을 경우, class='if'는 하나만 있는 것 확인함
            people_job = soup.select('.if')
            ppl_job_txt = people_job[0].string.encode('utf-8')
            

    # list type 일때는 id 순서로 출력 되었으나, dic type으로 바꾸면서 순서 엉망됨.
    print keyword,
    sheet1.write(row_index, 0, keyword)
    
    h2_str={}
    for (title,num) in h2_tag.items():
        title_txt = title.get_text()
        if title_txt in except_cate:
            del title_txt
        else:
            title_enc = title_txt.encode('utf-8')
            h2_str[title_enc] = num
        
    # sort 하면서 어쩔 수 없이 list type으로 바뀜
    #h2_sort = sorted(h2_str.iteritems(), key=operator.itemgetter(1))

    for (name,rank) in h2_str.items():
        if name == people_cate.encode('utf-8'):
            sheet1.write(row_index, rank+1, '%s(%s)' %(name, ppl_job_txt))   
        else:
            sheet1.write(row_index, rank+1, name)

book.save('naver_result_Gingerbread.xls')
        
    

    


        
    

    
    
   
