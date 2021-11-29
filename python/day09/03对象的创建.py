# 1、对象的创建 *****
#   1、格式：对象名=类名()
#   2、类在本文件定义，对象也在本文件定义
#   3、类在别的文件定义，对象在本文件定义
#   4、__init__在创建对象时，会被自动调用
class Maker():
    name = 'wxk'
    age = 18
    sex = '女'
    def printMaker(self):
        print('类的方法')
m = Maker()
print(m)


class Maker2():
    def __init__(self):
        print('有对象')
mm = Maker2()

# 2、调用属性：（用对象来调用类中的属性）
#   1、属性：生命在类中的变量，也叫类属性
#   2、调用：对象名.属性名
#   3、给类属性赋值：对象名.类属性=值
#   4、对象属性：通过对象名添加的属性，特点是只有这个对象可以使用
# 格式：对象.类中没有的属性名=值

class Test():
    name ='aaa'
    def printTest(self):
        print('Test')
# 定义一个对象
t = Test()
