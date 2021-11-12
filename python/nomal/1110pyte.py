import allure
import pytest


# 在终端运行 输入  allure serve ./reports/ 即可生成测试报告

# def fun(x):
#     return x + 1
# def test_func():
#     assert fun(4) == 5

class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x
    def test_two(self):
        x = 'hello'
        assert hasattr(x,'check')

if __name__ == '__main__':
    pytest.main(['--alluredir','./reports','1110pyte.py'])
          