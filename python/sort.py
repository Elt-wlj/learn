# -*- coding: utf-8 -*-
import random

# L = [('Boaaab', 75), ('Adm', 92), ('Bart', 66), ('1Lisa', 88)]

class test:
    def __init__(self,a,b,name):
        self.a=a
        self.b=b        
        self.name=name        
    def sss(self):
        return random.randint(0,9)
    def bbb(self):
        return self.b
# L=[{
#     "name":"wlj",
#     "a":1,
#     "b":2
# },{
#     "name":"cly",
#     "a":2,
#     "b":1
# }]

L=[test(1,2,'cly'),test(2,1,'wlj')]
# a=test(1,2)
# print(a.a)
# print(L)

def by_name(t):
    # return t[1]
    # a=random.randint(0,9)
    # print(t)
    return t.a

L2 = sorted(L, key=by_name)
# print(L2)
for a in L2:
    print(a.name)
# # by_name
# def sort1ed(L,key):
#     for t in L:

#         x=key(t)
