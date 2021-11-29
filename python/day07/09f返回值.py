# 返回值 return后没有什么语句返回none
# 可以返回数值，返回变量、表达式、
# 函数内碰到return，表示函数就结束
def test(): # 返回变量
    s = 10+20
    return s
print(s)

# 函数可以返回多个值
def test1(): # 什么都没返回
    return 
print(test1())

def test02(): # 返回数值
    return 10,20,30
print(test02())

def test2():  # 返回表达式
    a =10
    b=20
    return a > b
print(test2())  