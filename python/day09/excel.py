# 1、引用包
import xlrd
from xlrd import sheet
# 2、打开文件
workbook = xlrd.open_workbook(r'aa.xls')
# 3、获取打开的sheet文件
# 获取所有的sheet文件
sheet_name = workbook.sheet_names()[0]
sheet = workbook.sheet_by_index(0)
print(sheet.name,sheet.nrows,sheet.ncols)
rows = sheet.row_values(1)
print(rows)
