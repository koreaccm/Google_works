#-*- coding: utf-8 -*-
import urllib, urllib2
import StringIO, gzip
#to read xls file
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
    params = {'q':keyword}
    enc_params = urllib.urlencode(params)
    
    #검색결과 페이지에 우측 박스가 나오지 않는다. url parameter가 빠져서 그런 것으로 추정 중
    request = urllib2.Request('https://www.google.co.kr/'+'search'+'?'+enc_params)
    request.add_header('User-agent', 'Mozilla/5.0')
    request.add_header('Accept-encoding', 'gzip')
    response = urllib2.urlopen(request)

    compressedstream = StringIO.StringIO(response.read())
    gzipper = gzip.GzipFile(fileobj=compressedstream)

    data = gzipper.read().encode('utf-8')
    
    if (data.find('knop') != -1 ):    
        sheet1.write(row_index,6,'yes')
        book.save('result.xls')
        book.save(TemporaryFile())
        
        print 'yes'
    else:
        print 'no'
   
    