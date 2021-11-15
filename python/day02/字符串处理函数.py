# 获取字符串的长度用len()
str1 ='hello world'
print(len(str1))  

# 获取子串出现的次数  counr(子串,beg=0,end=len(母串))
str2='hello'
str3 = 'hello world abc hello 123'
a = str3.count(str2,0,9)
print(a)

# 让字符串变量中的转义失效
mystr= 'weixi\\n123'
print(repr(mystr)) # weixin\\n123  目的：输出两个\\

# 替换
name='wxk'
print(name.replace('wxk','123',1)) 