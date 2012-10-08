# example 1
from xlrd import open_workbook
wb = open_workbook('test.xls')
for s in wb.sheets():
    print 'Sheet:',s.name
    for row in range(s.nrows):
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print ','.join(values)
    print
    

# example 2
from xlrd import cellname

book = open_workbook('test.xls')
sheet = book.sheet_by_index(0)
print sheet.name
print sheet.nrows
print sheet.ncols

for row_index in range(sheet.nrows):
    for col_index in range(sheet.ncols):
        print cellname(row_index, col_index), '-',
        print sheet.cell(row_index, col_index).value
    
#example 3
from xlrd import XL_CELL_TEXT

book = open_workbook('test.xls')
sheet = book.sheet_by_index(0)

cell = sheet.cell(0, 0)
print cell
print cell.value
print cell.ctype==XL_CELL_TEXT

for i in range(sheet.ncols):
    print sheet.cell_type(0,i), sheet.cell_value(0,i)
    
#example 4
book = open_workbook('test.xls')
sheet0 = book.sheet_by_index(0)

print sheet0.row(0)
print sheet0.col(0)
print
print sheet0.row_slice(0,1)
print sheet0.row_slice(0,1,2)
print sheet0.row_values(0,1)
print sheet0.row_values(0,1,2)
print sheet0.row_types(0,1)
print sheet0.row_types(0,1,2)
print
print sheet0.col_slice(0,1)
print sheet0.col_slice(0,1,2)
print sheet0.col_values(0,1)
print sheet0.col_values(0,1,2)
print sheet0.col_types(0,1)
print sheet0.col_types(0,1,2)







    