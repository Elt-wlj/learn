import pytest
@pytest.fixture
def head():
    print('测试用例开始执行')
    yield
    print('测试用例结束')