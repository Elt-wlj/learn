# 导入webdriver
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
# driver.execute('GET', {'url':'http://www.baidu.com'})

driver.find_element_by_xpath().send_keys()