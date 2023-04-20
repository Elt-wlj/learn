import os
import pandas as pd

file_name_all = os.listdir(r'D:\1\2')
# print(file_name_all)
result = []
y = '折扣金额明细'
for file_name in file_name_all:
    file_path_li = os.path.join(r'D:\1\2', file_name)
    all_data = pd.read_excel(file_path_li, sheet_name=None, dtype='string')
    # print(all_data)

    xl = pd.ExcelFile(file_path_li)
    sheet_names = xl.sheet_names
    df = xl.parse(sheet_names)
    x = df.keys()
    # print('-----------',x)
    for same_sheet_name in x:
        if same_sheet_name == y:
            writer = pd.ExcelWriter("test.xlsx")
            result.append(all_data[same_sheet_name])
            print('result-------------',result)
            group_data = pd.concat(result)
            group_data.to_excel(writer,sheet_name=same_sheet_name)

writer.close()