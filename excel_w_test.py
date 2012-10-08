#-*- coding: utf-8 -*-
#example 1_simple
from tempfile import TemporaryFile
from xlwt import Workbook

book = Workbook()
#added option (example 2)
sheet1 = book.add_sheet('Sheet 1',cell_overwrite_ok=True)
book.add_sheet('Sheet 2')

sheet1.write(0,0,'A1')
sheet1.write(0,1,'B1')
#added option (example 2)
sheet1.write(0,1,'overwritten')
row1 = sheet1.row(1)
row1.write(0,'A2')
row1.write(1,'B2')
sheet1.col(0).width = 10000

sheet2 = book.get_sheet(1)
sheet2.row(0).write(0,'Sheet 2 A1')
sheet2.row(0).write(1,'Sheet 2 B1')
#이건 뭔지 모르겠
sheet2.flush_row_data()
sheet2.write(1,0,'Sheet 2 A2')
sheet2.col(0).width = 5000
sheet2.col(0).hidden = True

book.save('excel_w_ex1&2.xls')
book.save(TemporaryFile())



