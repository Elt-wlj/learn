# 1、split 截取字符串
str1="快乐的小宝贝,啦啦啦"
a = ','
print(str1.split(a)) #函数返回的是列表
print(str1.split(a)[1])# 打印啦啦啦
print(str1.split(a,1))# 把整个字符串以逗号分为3大段

#2、 获取子串的位置
# str.find(子串,开始位置,结束位置);从字符串中查找子串所在的位置，没找到返回-1
print(str1.find('我')) # 从第一次出现的位置从0开始查找

# 3、index
print(str1.index('我')) # 如果该字符串没有出现在字符串，中就会报异常