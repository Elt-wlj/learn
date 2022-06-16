from selenium import webdriver
import unittest,os,time
from time import sleep
# 增加鼠标点击事件
from selenium.webdriver.common.action_chains import ActionChains
# 增加键盘点击事件
from selenium.webdriver.common.keys import Keys


class GzTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        url = 'http://192.168.1.76:8080/macp/index.html'
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def login(self,user,pwd):
        self.driver.find_element_by_id('LAY-user-login-username').send_keys('guest001')
        sleep(3)
        self.driver.find_element_by_id('LAY-user-login-password').send_keys('Qwer1234')
        self.driver.find_element_by_id('login').click()
        sleep(3)


    def add_test_01(self):
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

        # # 判断结果
        # result = self.is_login_success()
        # self.assertTrue(result)

    # 摄像头管理模块下-----详细功能模块
    def test_03(self):
        # 摄像头的删除
        self.login('guest001','QWer1234')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(1)
        # 点击视频AI
        self.driver.find_element_by_link_text('视频AI').click()
        sleep(1)
        self.driver.find_element_by_link_text('摄像头管理').click()
        sleep(3)
        # 切换iframe
        self.driver.switch_to.frame('bodyFrom')
        sleep(1)
        self.driver.find_element_by_xpath('//div[@class="layui-card-body"]/div/div/div[2]/table/tbody/tr[1]/td[10]/div/a[5]').click()
        sleep(3)
        # 点击删除的是按钮
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(1)
        # 点击删除的否按钮
        # self.driver.find_element_by_class_name('layui-layer-btn01').click()
    #工控设备的增加
    def add_test_04(self):
        # 工控设备的增加
        self.login('guest001','QWer1234')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(1)
        # 点击视频AI
        self.driver.find_element_by_link_text('视频AI').click()
        sleep(1)
        self.driver.find_element_by_link_text('工控机设备管理').click()
        sleep(3)
        # 切换iframe
        self.driver.switch_to.frame('bodyFrom')
        # # 释放iframe
        # self.driver.switch_to.default_content()
        # sleep(1)
        # 点击新增
        self.driver.find_element_by_id('camerAdd').click()
        # 再次进行切换iframe
        # self.driver.switch_to.frame('layui-layer-iframe')
        # sleep(1)
        # 点击选择机构名称
        self.driver.find_element_by_xpath('//div[@class="layui-card"]/div/div/div').click()
        sleep(2)
        # 选择机构名称下的第一条数据
        self.driver.find_element_by_xpath('//div[@class="layui-card"]/div/div/div/dl/dd[2]').click()
        # 盒子名称
        self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]/div/form/div/div[2]/div/input').send_keys('测试盒子')
        # 盒子IP
        self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]/div/form/div/div[3]/div/input').send_keys('192.168.1.37')
        # 信号通道
        self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]/div/form/div/div[4]/div/input').send_keys('0')
        sleep(1)
        # 点击保存的按钮
        self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]/div/form/div[2]/button').click()
        sleep(1)
    
    # 工控机设备的删除
    def del_test_05(self):
        # 摄像头的删除
        self.login('guest001','QWer1234')
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(1)
        # 点击视频AI
        self.driver.find_element_by_link_text('视频AI').click()
        sleep(1)
        self.driver.find_element_by_link_text('工控机设备管理').click()
        sleep(3)
        # 切换iframe
        self.driver.switch_to.frame('bodyFrom')
        # # 释放iframe
        # self.driver.switch_to.default_content()
        # sleep(1)
        # 点击工控机设备下的删除按钮
        self.driver.find_element_by_xpath('//div[@class="layui-table-box"]/div[2]/table/tbody/tr/td[5]/div/a').click()
        sleep(3)
        # 点击弹窗中的否按钮
        # self.driver.find_element_by_class_name('layui-layer-btn1').click()
        # 点击弹窗中的是按钮
        self.driver.find_element_by_class_name('layui-layer-btn0').click()
        sleep(3)
    #截图的保存
    def saveScreenShot(self):
        if not os.path.exists('./report/images'):
            os.mkdir('./report/images')
        # 根据当前的时间生成相应的测试报告名字
        now = time.strftime('%Y-%m-%d_%H_%M_%S')
        # 截图保存
        imgpath = os.path.join('./report/images','%s.png' % str(now))
        self.driver.save_screenshot(imgpath)

        print('screenshot:',now,'.png')
        sleep(1)

    
    def is_login_success(self):
        try:
            name_ = self.driver.find_element_by_id('userName').text
            print(name_)
            return True
        except:
            self.saveScreenShot()
            # return False
    
    def tearDown(self) -> None:
        self.driver.quit()


