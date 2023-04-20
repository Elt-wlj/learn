import json

import xlrd
import jsonpath

from xlutils import copy
from openpyxl import load_workbook


class Read_Excel:
    def __init__(self, excel_path, sheet_name) -> None:
        self.sh = load_workbook(excel_path)
        self.wb = self.sh[sheet_name]

    def Read_excel(self):
        all_data = []
        data = list(self.wb.values)
        key = data[0]
        for row in data[1::]:
            x = row[0]
            self.write_result(x=row)
            row_dict = dict(zip(key, row))
            all_data.append(row_dict)
            return x
        return all_data

    def write_result(self, file, row, cols, result):
        excel_data = xlrd.open_workbook(file, formatting_info=True)
        wbook = copy.copy(excel_data)
        # 从wbook对象中获取第一个sheet对象
        sheet_copy = wbook.get_sheet(1)
        # 向sheet的某个单元格写入值
        sheet_copy.write(row, cols, result)
        # 写入完成后保存data的copy对象
        wbook.save(file)
        return self


if __name__ == '__main__':
    excel_path = r'D:\cpy-code\dd\lx\aze_api.xlsx'
    file_path = r'D:\cpy-code\dd\lx\aze_api.xls'
    re = Read_Excel(excel_path, 'Me')
    print(re.Read_excel())
    re.write_result(file_path,1,8, 'Pass')
