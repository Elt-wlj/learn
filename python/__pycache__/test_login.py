import unittest
import  time
from selenium import  webdriver

class EduLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)
        self.driver.get(r"http://122.112.142.111:9203/login")
        time.sleep(2)
    def test_login_success(self):
        # 输入用户名
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control']/span/span/input").send_keys("csdean")
        # 输入密码
        self.driver.find_element_by_xpath("//form/div[4]/div/div/span/span/input").send_keys("111111")
        # 点击登录按钮
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control']/span/button").click()
        # login_info=self.driver.find_element_by_class_name("username").text
        # print('此账号是教育大屏的账号')
        try:
            self.assertIn("csdean",'csdean')
            self.assertIn("111111","111111")
        except AssertionError as e:
            print("登录失败")
            #截图
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".","_"))
            raise
        time.sleep(2)
        # 点击教学视频按钮
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[2]/div").click()
        time.sleep(2)
        # 点击教学管理
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[3]/div").click()
        time.sleep(2)
        # 点击考试管理
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[4]/div").click()
        time.sleep(2)
        # 点击统计分析
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[5]/div").click()
        time.sleep(2)
        # 实验室管理
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[6]/div").click()
        time.sleep(2)
        # 基础设置--展开
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[7]/div").click()

        time.sleep(2)
        # 系统设置
        self.driver.find_element_by_xpath("//div[@class='ant-layout-sider-children']/ul/li[8]/div").click()
        time.sleep(2)
    def test_login_fail(self):
        # 输入用户名
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control']/span/span/input").send_keys("qwe")
        # 输入密码
        self.driver.find_element_by_xpath("//form/div[4]/div/div/span/span/input").send_keys("123456")
        # 点击登录按钮
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control']/span/button").click()
        # login_info=self.driver.find_element_by_class_name("username").text
        try:
            self.assertIn("zz002",'qwe')
            self.assertIn("111111","111111")
        except AssertionError as e:
            print("登录失败")
            #截图
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".","_"))
            raise
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()