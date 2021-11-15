# ==是否相等

# 三目运算符
# 格式：
# if 为真返回变量1 ，否则返回变量2
# （变量1 if(变量1 > 变量2) else 变量2） 
# 输入三个数，输出最大者
a = int(input('输入第一个数'))
b = int(input('输入第二个数'))
c = int(input('输入第三个数'))
s= (a if a> b else b)
print(s if s > c else c)
