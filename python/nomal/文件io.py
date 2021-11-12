# 文件的输入和输出
# 读取文件
# 打开一个文件
# fo = open('python3字符串.md','r')
# print('文件名：',fo.name)
#关闭文件
# fo.close()

# 写入文件操作---write()方法
# fo = open('te.txt','w')
# fo.write('123456789qwertyuiasdzxc')

# read()方法
# fo = open('te.txt','r+')
# str = fo.read(10)
# print('读取的字符串是：',str)



# 根据输入的数，进行一个排序输出。
# n = input("请输入一个整数：")
# for str in range(0,int(n)):
#     str=str+1
#     print(str)

# f.read()读取文件内容
# f = open("test.txt",'r',encoding='utf-8')
# str = f.read()
# print(str)

# f.readline()读取文件一行的内容
# f = open("test.txt",'r',encoding='utf-8')
# str = f.readline()
# print(str)


# f.readlines()返回所有的数据，旨在一行展示。
# f = open("test.txt",'r',encoding='utf-8')
# str = f.readlines()
# print(str)

# 1、f.write() 是将str写入到文件中，然后返回写入的总共数据的数量
# f = open("test.txt",'w',encoding='utf-8')
# num = f.write("在这是新写入的文件内容。。。")
# print(num)


# f.tell()返回对象 当前所处的位置，从文件开始算

# f.seek()查找文件
# f = open("test.txt",'rb+',encoding='utf-8')
# str = f.write(b'0123456abcdef')
# print(str)
# str2 = f.seek(5)
# print(str2)



# pickle模块，实现基本数据序列和反序列化


# 关闭打开的文件
# f.close()