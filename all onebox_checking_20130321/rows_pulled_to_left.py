#-*- coding: utf-8 -*-
from xlrd import open_workbook

filename = 'naver_result_iOS'
xls = open_workbook(filename+'.xls')
sheet0 = xls.sheet_by_index(0)

#to write in xls file
from tempfile import TemporaryFile
from xlwt import Workbook
        
book = Workbook()
new_sheet = book.add_sheet('arranged to left', cell_overwrite_ok=True) 


for row_index in range(sheet0.nrows):
    cell_list = []
    for col_index in range(sheet0.ncols):
        cell = sheet0.cell(row_index, col_index)
        cell_list.append(cell.value)
        cell_filtered = filter(None,cell_list)
        for col_index2 in range(len(cell_filtered)):
            new_sheet.write(row_index, col_index2, cell_filtered[col_index2])
        
        #new_sheet.write(row_index, col_index, cell.value)

book.save(filename+'_arranged.xls')
