from test2 import IwebshopLoginTest
from tools.HTMLTestRunner import HTMLTestRunner
import unittest
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(IwebshopLoginTest))
 
with open("./reports/login.html","wb") as f:
    h=HTMLTestRunner(stream=f,title="测试报告",description="windows Firefox")
    h.run(suite)