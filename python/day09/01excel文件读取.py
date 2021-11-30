# 1、包含xls和xlsx两种文件格式，读的方式一样，只是文件的后缀名不一致,
# 2、pip install xlrd  //// ，必须要安装1.2.0的版本才看可以显示数据，其他版本的是不可以的pip install xlrd==1.2.0
# 3、引入import xlrd
import xlrd

# 读取aa.xls的文件内容

# index的数值表示xlsx中的第几页，从0开始数
def read_xls(path,index):
    ex = xlrd.open_workbook(path) # 打开文件
    sh =ex.sheets()[index] #获取从index的行对象
    return sh

table = read_xls(r'aa.xls',0) # 这个1代表是sheet1还是sheet2表格

for i in range(0,table.nrows): # tanle_nrows代表的是总行数
    rows = table.row_values(i) #获的一行数据，以列表形式
    print(rows)
