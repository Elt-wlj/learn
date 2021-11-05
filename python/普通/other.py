# import requests
# result = requests.post('http://192.168.1.42/bank-kpi/sys/login')
# data={"username":"admin","password":"uaaIHVXKz5plwekhq/yK6w=="}
# print(result.json())
def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))