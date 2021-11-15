a = 'A'
# isdigit()纯数字则返回True，否则返回False
print(a.isdigit()) # False
# 只有大写字母才为真
print(a.isupper())
# 只有小写字母才为真
print(a.islower())
# 只有纯空格才是True
print(a.isspace())
# 为纯字母的时候才为True
print(a.isalpha())
# 为字母或数字时才为Ture
print(a.isalnum())

pwd = input('请输入密码:')
print(pwd.isalnum())