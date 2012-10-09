#-*- coding: utf-8 -*-
import urllib, urllib2
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
    params = {'query':keyword}
    enc_params = urllib.urlencode(params)
    
    request = urllib2.Request('http://search.chosun.com/search/'+'total.search'+'?'+enc_params)
    request.add_header('User-agent', 'Mozilla/5.0')
    response = urllib2.urlopen(request)
    data = response.read().encode('utf-8')
    #aceept-encoding: gzip을 사용하지 않아서 관련된 코드와 모듈 모두 제거
            
    if (data.find('<!-- 포커스 인물') != -1 ):    
        sheet1.write(row_index,4,'yes')
        book.save('result.xls')
        book.save(TemporaryFile())
        
        print 'yes'
    else:
        sheet1.write(row_index,4,'no')
        book.save('result.xls')
        book.save(TemporaryFile())
        
        print 'no'
        
    
    
    