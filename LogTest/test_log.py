from asyncio.log import logger
from login import TestEven
from mylogger import Logger, MyLogger
# log日志的生成
class Event_login:
    def __init__(self,case_name,case_expected):
        logger.info('一条测试用例:{}'.format(case_name))
        self.case_name=case_name
        self.case_expected=case_expected
        self.case_actual = None
    # 测试用例的编写
    def run_case(self,input_x,even_x):
        logger.info('用例数据为：ID{},按钮{}'.format(input_x,even_x))
        if input_x != 'su':
            self.case_actual ='点击输入框出错'
            return 
        if even_x != 'kw':
            self.case_actual = '点击按钮出错'
            return 
        if input_x =='su' and even_x == 'kw':
            self.case_actual = '百度搜索成功!!!!'
        logger.info('用例运行完成，运行结果为:{}'.format(self.case_actual))
       
    def case_resu(self):
        if self.case_actual != self.case_expected:
            # 实际结果与期望值不一样
            logger.error('实际与预期结果不一致,未通过')
        else:
            # 测试用例通过
            logger.error('该用例通过!!!!!!')


test1= TestEven()
ix,ex = test1.test()
res = Event_login('输入内容','点击按钮')
res.run_case(ix,ex)
res.case_resu()
