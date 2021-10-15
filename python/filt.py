# 1、在一个list中，删掉偶数，只保留奇数、
# def is_odd(n):
#     return n % 2 ==1
# print(list(filter(is_odd,(1,2,3,4,5,6,7))))

# 2、删除序列中的空字符串
# def not_empty(s):
#     return s and s.strip()
# print(list(filter(not_empty,(' ','A',' B','C   '))))

# 3、计算素数的方法是埃氏筛选法。

'''
这是一个生成器，并且是一个无限序列
'''
# def old_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
'''
定义筛选函数：
'''
# def not_divisible(n):
#     return lambda x : x % n >0

'''
定义生成器，不断返回下一个素数，这个生成器先返回第一个素数2，然后利用filter()不断筛选新的序列。
primes()是一个无限序列，所以需要设置一个退出循环的条件
带yield的就是一个函数的生产器
'''
# def primes():
#     yield 2 
#     it = old_iter()# 初始序列
#     while True:
#         n = next(it) # 返回序列的第一个数
#         yield n
#         it = filter(not_divisible(n),it) # 构建新的序列
    
# 打印1-1000以内的所有素数
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


#4、练习，回数从左向右，从右向左也是一样的数字eg(12321)
def is_palindrome(n):
    return str(n)==str(n)[::-1]
output = filter(is_palindrome,range(1,1000))
print('1--1000:',list(output))

    