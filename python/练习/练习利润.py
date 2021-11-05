# x < 10  10%
#  10 < x < 20  7.5%
# 20 < x < 40 5%
# 40 < x < 60 3%
# 60 < x < 100  1.5%
# x > 100 1%

pro = int(input("请输入您的利润金额："))
if  pro < 100000:
    y =pro *  0.01
elif 100000<= pro < 200000:
    y = pro *  0.01 + pro * 0.075
elif 200000<= pro < 400000:
    y = pro *  0.01+ pro * 0.075 + pro * 0.05
elif 400000<= pro < 600000:
    y = pro *  0.01+ pro * 0.075 + pro * 0.05 + pro * 0.03
else:
     y = pro *  0.01+ pro * 0.075 + pro * 0.05 + pro * 0.03 + pro * 0.15
print(y)

# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print ((i-arr[idx])*rat[idx])
#         i=arr[idx]
# print (r)