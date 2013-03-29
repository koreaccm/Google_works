#-*- coding: utf-8 -*-
from xlrd import open_workbook

filename = 'naver_result_Gingerbread'
xls = open_workbook(filename+'.xls')
sheet0 = xls.sheet_by_index(0)

#to write in xls file
from tempfile import TemporaryFile
from xlwt import Workbook
        
book = Workbook()
new_sheet = book.add_sheet('arranged to left', cell_overwrite_ok=True) 
cell_list = []

for row_index in range(sheet0.nrows):
    for col_index in range(sheet0.ncols):
        cell = sheet0.cell(row_index, col_index)
        cell_list[col_index] += cell.value
        cell_filtered = filter('',cell_list)
        
        
        #new_sheet.write(row_index, col_index, cell.value)

book.save(filename+'_arranged.xls')