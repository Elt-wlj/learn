# 功能逻辑

def login_check(input_x=None,even_x=None):
    if input_x !=None and even_x !=None:
        if input_x == 'su' and even_x == 'kw':
            return {'code':1,'msg':'百度搜索成功！'}
        else:
            return {'code':1,'msg':'百度搜索失败'}
    else:
        return {'code':1 ,'msg':'取值错误'}

