import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
global_path = os.path.join(path, '2')


class SameDateWrite:
    def __init__(self, excel_path, extract_name):
        self.file_name_path = os.listdir(excel_path)
        self.sheet_name = extract_name

    def write_data(self):
        # 定义初始文件为空
        result = []
        for file_name in self.file_name_path:
            # 读取excel中的所有文件
            file_path_li = os.path.join(global_path, file_name)
            all_data = pd.read_excel(file_path_li, sheet_name=None, dtype='string')
            # 获取文件名
            get_excel_name = pd.ExcelFile(file_path_li)
            # 获取sheet_name
            sheet_name = get_excel_name.sheet_names
            all_sheet_name = get_excel_name.parse(sheet_name).keys()
            for same_sheet_name in all_sheet_name:
                if same_sheet_name == self.sheet_name:
                    writer = pd.ExcelWriter("test.xlsx")
                    result.append(all_data[same_sheet_name])
                    print('result-------------', result)
                    # 将同名数据进行拼接
                    group_data = pd.concat(result)
                    # 保存到工作簿中，指定工作标名为same_sheet_name
                    group_data.to_excel(writer, sheet_name=same_sheet_name)
        writer.close()
        # return group_data


if __name__ == '__main__':
    sd = SameDateWrite(r'D:\1\2', '折扣金额明细')
    sd.write_data()
