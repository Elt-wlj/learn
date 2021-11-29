from test_login import EduLoginTest
from tools.HTMLTestRunner import HTMLTestRunner
import unittest
suite = unittest.TestSuite()
suite.addTests(unittest.makeSuite(EduLoginTest))
with open("./reports/LoginTest.html","wb") as f:
    h=HTMLTestRunner(stream=f,title="登录测试报告",description="windows Chrome")
    h.run(suite)