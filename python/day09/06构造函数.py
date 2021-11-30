# 构造函数
# 1、构造函数时给对象的实例变量赋初始值
# 2、当一个对象被创建的时候，第一个被自动调用的函数
# 3、语法：
# __init__(参数列表)：
    # 函数体
# 4、构造函数的参数在定义对象时传递，如：m=Maker (实参) ->实参传递到__init__(形参)
# 5、如果没有显示定义构造函数，那么系统默认提供一个无参的构造函数，这个无参的构造函数时空函数体。手动添加了有参的构造函数之后，系统将不再提供构造函数 *****
# class Maker():
#     def __init__(self):
#         print('该函数在创建对象时调用')
#         self.name = '123'
#         self.age = 18

# m=Maker()
# print(m.name)
# print(m.age)

class Maker2():                                                                                  
    def __init__(self,name):
        print('有参构造函数')
        self.name = name
    # def __init__(self): # 一个类中不饿能有2个init函数
    #     print('无参构造函数')

m2=Maker2('李四')
print(m2.name)
m3 = Maker2()

