import requests

# 接口的url
url = r"http://fanyi.baidu.com/v2transapi"

# 接口的参数
params={
    "from":"en", 
    "to":"zh", 
    "query": "test"
}

# # 发送接口
r = requests.request("post",url,params=params)

# # 打印返回结果
# print(r.text)

import json
d = json.loads(r.text)
print(d['liju_result']['tag'])