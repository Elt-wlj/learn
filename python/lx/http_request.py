import requests

class MyRequest:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
    
    def send_request(self,method,url,data,token=None):
        if method.upper() == "Get":
            resp = requests.request(method,url,param=data,headers = self.headers)
        else:
            resp = requests.request(method,url,json=data,headers = self.headers)
        return resp

if __name__ == '__main__':
    mq = MyRequest()
    method = "post"
    url = ' https://go.sztnh.com/gateway/servicebus-fssapi/fssapi/auth/sign-in'
    req_data = {
        "identifier": "lynn@sztus.com",
          "password": "c3bb4e958cc1c7d98b59d9ec06b6c2a9",
          "portfolioId": 110
    }
    resp1 =mq.send_request(method,url,req_data)
    print(resp1.json())
    