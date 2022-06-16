from time import sleep
from head import GzTest
import unittest
from selenium import webdriver

class GN_CamDetail(unittest.TestCase):
    def test_02(self):
        # cam = GzTest()
        # cam.Camera_anagement(self)
        self.login('guest001','QWer1234')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(1)
        # 点击视频AI
        self.driver.find_element_by_link_text('视频AI').click()
        sleep(1)
        self.driver.find_element_by_link_text('摄像头管理').click()
        sleep(3)
        # This is the first row of data
        # 切换iframe
        self.driver.switch_to.frame('bodyFrom')
        # # 释放iframe
        # self.driver.switch_to.default_content()
        # sleep(1)
        # 点击新增
        self.driver.find_element_by_id('camerAdd').click()
        # 再次进行切换iframe
        self.driver.switch_to.frame('layui-layer-iframe1')
        sleep(1)
        #点击机构名称，下拉请选择
        self.driver.find_element_by_class_name('layui-select-title').click()
        sleep(2)
        # 选择营业部这一条数据
        self.driver.find_elements_by_xpath('//div[@class="layui-input-inline"]/div/dl/dd')[1].click()
        # $x('//div[@class="layui-input-inline"]/div/dl/dd')[1]
        sleep(2)
        # 选择摄像头位置,点击请选择按钮
        # $x('//div[@class="layui-col-md12"]/div/div')[1]
        self.driver.find_elements_by_xpath('//div[@class="layui-col-md12"]/div/div')[1].click()
        sleep(2)
        # 选中大门口
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div/div[2]/div/div/dl/dd[2]').click()
        sleep(3)
        # 位置描述
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div/div[3]/div/input').send_keys('人数统计')
        print('人数统计写入成功')
        sleep(2)
        # This is the second line of data
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[2]/div/div/div/div').click()
        print('摄像头下的请选择点击成功')
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[2]/div/div/div/dl/dd[2]').click()
        sleep(2)
        print('摄像头---主摄像头')
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[2]/div[3]/div/div/div').click()
        print('监测是否关灯下请选择点击成功')
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[2]/div[3]/div/div/dl/dd[2]').click()
        sleep(2)
        print('检测状态--否')
        # This is the three line of data
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[3]/div/div/div/div').click()
        print('算力下的请选择')
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[3]/div/div/div/dl/dd[2]').click()
        print('选择第一个算力盒子')
        sleep(1)
        # This is the four line of data
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[4]/div/div').click()
        print('码流地址下的请选择')
        sleep(1)
        code_address = self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[4]/div/div/input')
        code_address.send_keys('rtsp://admin:HuaWei123@192.168.1.107:554/LiveMedia/ch1/Media1')
        print('码流地址-第一条数据')
        sleep(1)
        # This is the five line of data
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[5]/div/div/xm-select/div[2]').click()
        print('业务分类下的请选择')
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[5]/div/div/xm-select/div[3]/div/div/div/div[1]/i').click()
        print('选择第一个复选框-客户')
        sleep(1)
        # This is the six line of data
        self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[6]/div/div[1]/button').click()
        print('点击保存的按钮')
        # self.driver.find_element_by_xpath('//div[@class="layui-fluid"]/div/div[6]/div/div[2]/button').click()
        # print('点击取消的按钮')
        sleep(2)