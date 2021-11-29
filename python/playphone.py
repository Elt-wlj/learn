import time
from unicodedata import name 
import unittest
from unittest.main import main
from selenium import webdriver

class BankTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)
        self.driver.get(r'http://192.168.1.34:3001')
        time.sleep(3)
    def test_playphone(self):
        self.driver.find_element_by_id('username').send_keys('admin')
        self.driver.find_element_by_id('password').send_keys('123456')
        self.driver.find_element_by_xpath('//span[@class="ant-form-item-children"]/button').click()
        time.sleep(2)
        # 玩手机菜单栏的检测
        play=['玩手机检测']
        # 方法1
        self.driver.find_element_by_link_text('玩手机检测').click()
        # 方法2
        # self.driver.find_element_by_xpath('//div[@class="ant-layout-sider-children"]/ul/li[3]/a').click()
        # a = self.driver.find_element_by_xpath('//div[@class="ant-layout-sider-children"]/ul/li[3]/a/span').text
        # 获取点击列表中的文字，与实际需求的进行相比较，比对成功，执行下面的步骤。否则出错。
        a = self.driver.find_element_by_link_text('玩手机检测').text
        print(a)
        if a in play:
            print('玩手机菜单栏已检测到')
            # 此处是玩手机数据检测模块------top的数据内容
            deslist=[]
            play_top1 = self.driver.find_element_by_xpath('//div[@class="statistic-area"]/div[1]/div/div[2]').text
            play_top2 = self.driver.find_element_by_xpath('//div[@class="statistic-area"]/div[2]/div/div[2]').text
            play_top3 = self.driver.find_element_by_xpath('//div[@class="statistic-area"]/div[3]/div/div[2]').text
            play_top4 = self.driver.find_element_by_xpath('//div[@class="statistic-area"]/div[4]/div/div[2]').text
            deslist.append(play_top1)
            deslist.append(play_top2)
            deslist.append(play_top3)
            deslist.append(play_top4)
            print(deslist)
            cont=['今日','本周','待审核','分析柜台']
            if deslist == cont:
                print('玩手机页面数据-------测试用例通过')
                # 玩手机检测------minddle部分的内容
                
            else:
                print('该条测试用例不通过')
        else:
            print('玩手机菜单不存在,BUG....')
        time.sleep(2)
        # 大堂经理在岗检测
        duty=['大堂经理在岗检测']
        self.driver.find_element_by_link_text('大堂经理在岗检测').click()
        b = self.driver.find_element_by_link_text('大堂经理在岗检测').text
        print(b)
        if b in duty:
            print('大堂经理在岗检测菜单栏存在')
        else:
            print('大堂经理菜单栏不存在,BUG....')
        time.sleep(2)

        # 客流分析 ----下拉选择不能用文本链接的方式
        TrafStatis =['客流分析']
        self.driver.find_element_by_xpath('//div[@class="ant-layout-sider-children"]/ul/li[5]/div').click()
        c =self.driver.find_element_by_xpath('//div[@class="ant-layout-sider-children"]/ul/li[5]/div').text
        print(c)
        if c in TrafStatis:
            print('客流分析菜单栏存在')
            self.driver.find_element_by_link_text('今日客流分析').click()
            time.sleep(2)
            self.driver.find_element_by_link_text('历史客流分析').click()
            # print(d)
        else:
            print('客流分析菜单栏不存在,BUG....')
        time.sleep(2)
        try:
            self.assertIn("admin",'admin')
            self.assertIn("123456","123456")
        except AssertionError as e:
            print("登录失败")
            #截图 
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".","_"))
            raise
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
    