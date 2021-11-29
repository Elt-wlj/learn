a = 10 # 全局变量

def test01():
    b =20 # 局部变量,只能在test01中使用
    a = 100 # 自己定义的是局部变量，局部和全局重名时，函数内是局部变量
    print(a,b)
test01()

def test02():
    print(a)
    # print(b) 出错
test02()

# golabl b 这是表示函数内，引入全局变量，引入之后使用的是全局变量外的值
c=100
def test3():
    global c
    c = 1000
    print(c) #100
test3()
print(c)


# 不管是if还是for里面都是全局变量
for i in range(5):# 不是局部变量
    print(i)

def test04():
    print(i)
test04()