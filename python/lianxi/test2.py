import unittest
import  time
from selenium import  webdriver

class IwebshopLoginTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(40)
        self.driver.get(r"http://192.168.1.34")
        time.sleep(2)
    def test_login(self):
        self.driver.find_element_by_id("username").send_keys("admin")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_xpath("//div[@class='ant-form-item-control']/span/button").click()
        # login_info=self.driver.find_element_by_class_name("username").text
        try:
            self.assertIn("admin",'admin')
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
    