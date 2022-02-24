from check_login import login_check
import pytest
import allure
datas = [{'input_x':'su','even_x':'kw','check':{'code':0,'msg':'百度搜索成功!'}},
        {'input_x':None,'even_x':'kw','check':{'code':0,'msg':'取值错误'}},
        {'input_x':'su','even_x':None,'check':{'code':0,'msg':'取值错误'}},
        {'input_x':'su','even_x':'qq','check':{'code':0,'msg':'百度搜索失败'}},
        {'input_x':'ww','even_x':'kw','check':{'code':0,'msg':'百度搜索失败'}}]

@pytest.mark.usefixtures('head')
class SearchTest:
    @pytest.mark.parametrize('case',datas)
    def search(self,case):
        actual = login_check(case['input_x'],case['even_x'])
        assert actual == case['check']
@allure.title('模块测试开始')
def test_module():
    print('测试会话开始')