# 开始去超市购物
from selenium import webdriver
from time import sleep

# 定义工具类
class WebKeys:
    # 构造函数
    # 创建webdriver驱动
    def __init__(self):
        self.driver = webdriver.Chrome()
    # 访问URL
    def open(self,url):
        self.driver.get(url)
    # 退出
    def quit(self):
        self.driver.quit()
    # 元素定位
    def locator(self,name,value):
        return self.driver.find_element(name,value)
    # 输入
    def input(self,name,value,txt):
        el = self.locator(name,value)
        el.clear()
        el.send_keys(txt)
    
    # 强制等待
    def wait(self,time_):
        sleep(time_)

    # 断言
    def assert_art(self,word):
        try:
            art = self.driver.find_element_by_xpath().text       
            assert word in art
        except Exception as e:
            return e