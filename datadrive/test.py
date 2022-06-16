# # 使用数据驱动的方式进行
# import ddt
# import  unittest
# # 测试数据集
# testData= [{'LAY-user-login-username':'guest001','LAY-user-login-password':'Qwer1234'},
#             {'LAY-user-login-username':'guest001','LAY-user-login-password':'123456'},
#             {'LAY-user-login-username':'admin','LAY-user-login-password':'Qwer1234'}]
# @ddt.ddt
# class Test(unittest.TestCase):
#     def setUp(self) -> None:
#         print('start!')
#     def tearDown(self) -> None:
#         print('end!')

#     @ddt.data(*testData)

#     def test_ddt(self,data):
#         print(data)
# if __name__ == '__main__':
#     unittest.main()

# 根目录
from argparse import Action
import os
import re
import webbrowser


# Base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# report_dir = os.path.join(Base_dir,'report')
# print(Base_dir)
# print(report_dir)
# report_file = os.path.join(report_dir,'123.txt')
# print(report_file)


# from selenium.webdriver.common.action_chains import ActionChains
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome()
# url ='http://www.baidu.com'
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(30)
# Action=ActionChains(driver)
# sleep(3)
# aa = driver.find_element_by_id('s-usersetting-top')
# Action.move_to_element(aa).perform()

# driver.quit()


# # 导入驱动
# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys

# class Login_open():
#     # 浏览器的获取
#     driver = webdriver.Chrome()
#     # 打开网址
#     url = "http://192.168.1.34:3001/user/login"
#     driver.get(url)
#     # 设置浏览器的最大窗口
#     driver.maximize_window()
#     time.sleep(2)
#     driver.find_element_by_id('username').send_keys('001549')
#     driver.find_element_by_id("password").send_keys('123456')
#     driver.find_element_by_xpath("//*[@id='formLogin']/div/div[3]/div/div/span/button").click()
#     time.sleep(5)
#     driver.quit()

# # 业务质量管理模块 -打开
# # driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/div").click()
# # time.sleep(2)

# # # 业务服务列表页 -打开
# # driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[1]/a").click()
# # time.sleep(2)
# # # 服务质量总表 --打开
# # driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[2]/a").click()
# # time.sleep(2)
# # # 申诉处理
# # driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[3]/a").click()
# # time.sleep(2)
# # # 申诉结果
# # driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/ul/li[4]/a").click()
# # time.sleep(2)
# Login_open()

