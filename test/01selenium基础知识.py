# selenium 早期基于QTP实现的，
# 环境搭建：
    # 1、安装selenium
    # 通过pip insyall selenium 或者pycharm中的interpreter来进行安装
    # 2、webdriver安装
    # 通过下载安装chromedriver
    # firefox :geckodriver
    # 不管是什么类型的都要关闭自动更新


# webdriver+selenium 运行原理： 
# webdriver是一个服务端：

# 导图强制等待
# 方法一 from time import sleep
# sleep(5)
# 释放资源
# 方法二 import time
# time.sleep(5)
# driver.quit()


# 1、close和quite的区别
#   close 关闭当前页
#   quite关闭浏览器


# element not interactable 定位元素无法进行交互

