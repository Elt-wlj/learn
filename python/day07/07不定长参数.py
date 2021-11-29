# 不定长参数：一个函数能处理比当初声明时更多的参数
# 参数打包成元组给函数调用，如果在函数调用是没有指定参数，它就是一个空元组。
def func(name,*arr):
    print(name)
    for i in arr:
        print(i)
func('123',20.22,'d#@')

#
# n = input('请输入一个数字：')

def adds(*ak):
    s = 0
    for i in ak:
        s+=int(i)
    return s 
ss = adds(1,2,3,4,5)
print(ss)