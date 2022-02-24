from cgi import test
from selenium import webdriver
from time import sleep
class TestEven:
    def test(self):
        self.driver = webdriver.Chrome()
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        input_x = self.driver.find_element_by_id('su')
        input_x.send_keys('测试---软件测试')
        sleep(2)
        even_x = self.driver.find_element_by_id('kw')
        even_x.click()
        sleep(2)
        print(input_x)
        print(even_x)
        self.driver.quit()
        return input_x,even_x
        
        
# if __name__ == '__main__':
    # test()

# test1 = TestEven()
