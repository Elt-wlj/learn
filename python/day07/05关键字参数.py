# 关键字参数
def test(name,age):
    print('name-',name)
    print('age=',age)
test(age=18,name='wxk')

d = {'id':1,'name':'wxk','age':18,'iphone':123456}
def test2(id,name,age,iphone):
    print(id,age,name,iphone)

test2(d['id'],d['name'],d['age'],d['iphone'])