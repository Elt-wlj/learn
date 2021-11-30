
# 1、self 是对象自己，那个对象调用成员函数，那么解析器就把那个对象传递到成员函数中
# 如：
# class Maker():
#     def printMaker(self):
#         print('maker')
# m = Maker()
# m.printMaker()
#2、self有什么用？
#   当类变量和函数的形参同名时，可以区分函数的形参和类变量
#   可以区分局部变量和类变量
#   区分对象属性和局部变量
class Maker():
    name = '111'
    age = 18

    def printMaker(self,name,age):
        self.name = name
        self.age = age

    def test(self):
        name = 30
        self.name = 20

    def test2(self):
        print(self.score)
    
    # 如果类变量和对象属性重名时，那么这个就是类变量

    def test3(self):
        self.score2 = 200 # 对象属性，在成员函数内定义一个书香属性
m = Maker()
m.score = 100
m.test2()
m.test3()
print(m.score2)

    