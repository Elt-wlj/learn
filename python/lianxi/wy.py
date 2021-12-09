from selenium import webdriver
from time import sleep
# 打开浏览器的驱动
driver = webdriver.Chrome()
# 打开网址
url = driver.get("https://music.163.com/")
driver.maximize_window()

# 点击登录按钮：
driver.find_element_by_xpath("//a[text()='登录']/..").click()
sleep(3)
driver.find_element_by_id("otherbtn").click()
sleep(2)
driver.find_element_by_xpath("//input[@type='checkbox']").click()
sleep(1)
driver.find_element_by_xpath("//a[@data-type='netease']").click()
sleep(3)
driver.find_element_by_id("e").send_keys('wangpromise520@163.com')
sleep(2)
sleep(3)
driver.find_element_by_xpath("//input[@checked='checked']").click()

driver.find_element_by_id("epw").send_keys('linjie621808')

# 登录
driver.find_element_by_xpath("//div[@class='f-mgt20']/a").click()
sleep(2)

driver.close()



