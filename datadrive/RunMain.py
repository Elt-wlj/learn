import unittest
from time import sleep
from selenium import webdriver
import time
from tools.HTMLTestRunner import HTMLTestRunner
import os,shutil 

discover = unittest.defaultTestLoader.discover('./case',pattern='head.py')
# # 报告存放的地址
# # 获取到当前的目录
Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 获取report的路径
report_dir = os.path.join(Base_dir,'report')
# 根据当前的时间生成相应的测试报告名字
now = time.strftime('%Y-%m-%d_%H_%M_%S')

filename =now + '-result.html'
# # 把文件写入report中
# # report_file = os.path.join(report_dir,filename)
# # print(report_file)
     
with open(filename,'wb') as f:
    h = HTMLTestRunner(stream=f,title='贵州农信测试报告',description='贵州农信的测试',tester='Linjie Wang')
    h.run(discover)
    f.close()

# 移动文件到指定目录,如果文件不存在就创建文件。
dirs = 'report'
if not os.path.exists(dirs):
    os.makedirs(dirs)
    shutil.move(filename,'report')
else:
    shutil.move(filename,'report')

    

    