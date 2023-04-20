from openpyxl import load_workbook


class MyExcel:
    def __init__(self, excel_path, sheet_name):
        self.wb = load_workbook(excel_path)
        self.sh = self.wb[sheet_name]

    def read_excel(self):
        all_data = []
        data = list(self.sh.values)
        keys = data[0]
        for row in data[1::]:
            row_dict = dict(zip(keys, row))
            all_data.append(row_dict)
        return all_data


if __name__ == '__main__':
    excel_path = r"D:\cpy-code\dd\aze_api.xlsx"
    me = MyExcel(excel_path, 'Me')
    xx = me.read_excel()
    for item in xx:
        print(item)

