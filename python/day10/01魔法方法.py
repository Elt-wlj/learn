# 魔法方法
# 格式：___XXX___(self)
# xxx 代表很多：如
# add 加法(两个对象呢相加时调用)
# lt 小于(两个对象比较时调用)
# gt 小于(两个对象比较时调用)
# str 字符串(打印对象时调用)

# class Maker():
#     def __init__(self,v):
#         self.v = v
#     def __str__(self):
#         msg = ('我是模仿方法')
#         return msg
#     def __add__(self,other):
#         print('两个对象相加') # 当两个对象相加时，回去调用该函数
#         # return f'{self.v}{other.v}'
#         return self.v+other.v

# m = Maker('aaa')
# print(m)
# m2 = Maker('bbb')
# m+m2


# 定义一个魔法方法比较两个参数的大小

class Test():
    def __init__(self,v):
        self.v = v
    # def __lt__(self,other):

    #     if self.v < other.v:
    #         print('前面的更小')
    #     else:
    #         print('前面的更小')

    def __gt__(self,other):
    
        if self.v > other.v:
            print('前面的更大')
        else:
            print('前面的更小')

t = Test(900)
d = Test(200)
# t > d
t < d 