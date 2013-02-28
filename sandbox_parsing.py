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
sheet1 = book.add_sheet('result 1') 

    
for row_index in range(sheet0.nrows):

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
    
    #swicth case, class_ =""
    #minibox <span class="kno-sh">이것을 찾으셨나요?</span>
    #fullbox <div class="kno-ecr-pt">원빈</div>
    #출연작 if class="kno-sh ellip" 로 감싼 text 가 "출연작",  class="vrtr" children 개수저장
    #출연진, 출연자, 소속 그룹, 형제 자매, 여자형제, ... ---> 1k queries 결과값을 먼저 살펴볼 필요! 다른 파일에서 코드짜기  
    #함께 if class="kno-sh ellip" 로 감싼 text 가 "함께 찾은 검색어", class="vrtr"
    
    #minibox 1st URI parameter는 변칙적임. 1st url을 따로 저장해둘 필요 있음 
    
    #top onebox class는 sandbox class와 다름을 확인했음
    #bs 객체 수 카운트 방법은?
    #attribute div class = "kno-ft kno-xs", table class = "kno-fs ts"
    
    boxtag = soup.find_all(class_="kno-mec rhsvw kno-mecec kno-fb-ctx")
    print boxtag
    print request
        
    #if (boxtag == 'kno-ec rhsvw vk_rhsc kno-ec-si'):
    #   print boxtag.string
    #else:
    #    print 'none'
        
    
    
   
