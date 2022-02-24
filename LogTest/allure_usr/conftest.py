from selenium import webdriver
import time 
from time import sleep
import pytest

@pytest.fixture(scope="class")
def browser():
    # 前置的代码   
    print('------测试类下的测试用例开始执行------')
    driver = webdriver.Chrome()
    url = 'http://192.168.1.76:8080/macp/index.html'
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    # 后置清理工作的代码
    yield
    print('------类下的测试用例结束------')
    driver.quit()
    