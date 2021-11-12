import pytest
#定义登录函数
def login(username,password):
    """
    :param username: 用户名
    :param password: 密码
    :return:
    """
    if username=='admin' and password=='123456':
        print('登录成功')
        return username,password
    else:
        print('登录失败')
        return username,password

#设计测试用例
def test_login_001():
    """用户名和密码正确"""
    user_login=login('admin','123456')
    #使用assert判断用户是否登录成功
    assert(user_login==('admin','123456'))
@pytest.mark.failtest
def test_login_002():
    """用户名和密码为空"""
    user_login=login('','')
    #使用assert判断用户是否登录成功
    assert(user_login==('admin','123456'))
def test_login_003():
    """用户名正确，密码错误"""
    user_login=login('admin','1111')
    # 使用assert判断用户是否登录成功
    assert (user_login == ('admin','123456'))
def test_login_004():
    """用户名错误，密码正确"""
    user_login=login('haha','123456')
    # 使用assert判断用户是否登录成功
    assert (user_login == ('admin', '123456'))
def test_login_005():
    """用户名和密码都错误"""
    user_login=login('admin','111111')
    # 使用assert判断用户是否登录成功
    assert (user_login == ('admin', '123456'))


