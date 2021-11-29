# 如果形参有值，那么实参可以传，也可不传，默认使用形参的值，如果传，那么使用实参值
def func(name,age=18):
    print(name,age)
func('haha')

# 弱国形参有默认值，后面的参数也必须要有默认值
def func2(a,b,c=10,d=10):
    print(a,b,c,d)

