# 正则表达式
# import re

# print(re.match(r'^\d{3}\-\d{5}$','010-12345'))
# import re
# s = 'bob@example.com'
# def is_email():
#     return re.match(r'^([a-zA-Z\.]+)@([a-zA-Z0-9]+).com','bill.gates@microsoft.com')
# print(is_email())

# 时间转换
# from datetime import datetime 
# s = datetime.now()
# x = s.timestamp()
# xx = 1679710684
# print(x)
# print(datetime.fromtimestamp(xx))

# print(s.strftime('%a,%b %d %H:%M'))

# 读取xml文件格式
# from collections import namedtuple
# p = namedtuple('p',['X','Y'])
# pp = p(1,2)
# print(pp.x)
# import json
# from urllib import request
# import json
# def fetch_data(url):
#     req = request.Request(url)
#     req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36')
#     with request.urlopen(req) as f:
#         data = f.read().decode('utf-8')
#         d = json.loads(data)
#     return d
# URL = 'http://www.httpbin.org/get'
# data = fetch_data(URL)
# print(data)
# assert data['origin'] == '125.75.162.164'
# print('ok')


# from xml.parsers.expat import ParserCreate
# class DeSaxHand(object):
#     def start_element(self,name,attrs):
#         print('sta_elem:%s','Attr:%s'%(name,str(attrs)))
#     def end_element(self,name):
#         print('end_el:%s'%(name))
#     def char_data(self,text):
#         print('char_el:%s'%(text))

# xml = '''
# <?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>

# '''
# han = DeSaxHand()
# par = ParserCreate()
# par.StartElementHandler = han.start_element
# par.EndElementHandler = han.end_element
# par.CharacterDataHandler = han.char_data

# par.Parse(xml)

# 读取父进程
# import os
# pid = os.fork()
# if pid == 0:
#     print('child %s parent %s' %(os.getpid(),os.getpid()))
# else:
#     print('its just child %s'%os.getpid())

# 缩小图片尺寸
# from PIL import Image
# im = Image.open(f'D:\cpy-code\dd\img\1.jpg')
# w,h = im.size
# print('original size : {}'.format(w,h))
# im.thumbnail((w//2,h//2))
# print('resize size : {}'.format(w,h))
# im.save('2.jpg','jpg')


# import requests
# upload_file = {'file': open('1.xlsx','rb')}
# r = requests.post(url, files=upload_files)


# 绘画图像
# from turtle import *
# width(4)
# forward(200)
# right(90)
# pencolor('purple')
# forward(100)
# right(90)
# pencolor('green')
# forward(200)
# right(90)
# pencolor('blue')
# forward(100)
# right(90)
# done()

# 绘图五角星
# from turtle import *
# def drawStart(x,y):
#     pu()
#     goto(x,y)
#     pd()
#     for i in range(5):
#         fd(40)
#         rt(144)
# for x in range(0,250,50):
#     drawStart(x,0)

# done()

# tcp编程 
'''
AF_INET :  ipv4
AF_INET6: ipv6
SOCK_STREAM: 指定使用面向流的TCP协议
'''
import socket
import threading # 线程
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.connect(('www.baidu.com',80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# header,html = data.split(b'\r\n\r\n',1)
# print(header.decode('utf-8'))
# with open('ss.html','wb') as f:
#     f.write(html)
# import socket
# import threading
# #处理客户端请求
# def tcplink(sock,addr):
#     print('Accept new connection from %s:%s...' % addr)
#     sock.send('welcome!')
#     while True:
#         data=sock.recv(1024)
#         if data=='exit' or not data:
#             break;
#         sock.send('hello %s' % data)
#     sock.close()
#     print('Connection from %s:%s closed' % addr)
# s=socket.socket()
# s.bind(('127.0.0.1',9999))#绑定地址和端口
# s.listen(5)
# print('serve is waiting connect.....')
# while True:
#     sock,addr=s.accept()
#     #创建新线程来处理每个客户端连接
#     #target=tcplink代表新线程要运行哪个函数
#     #args=(sock,addr)代表向这个方法传的参数
#     t=threading.Thread(target=tcplink,args=(sock,addr))
#     #启动这个线程
#     t.start()




# 邮件的发送
# from email.mime.text import MIMEText
# msg = MIMEText('hello ,my friend','plain','utf-8')
# from_addr = input('From:2208078600@qq.com')
# password = input('Password:linjie621808@')
# to_addr = input('To: wangpromise520@163.com')
# smtp_server = input('SMTP: ','https://mail.qq.com/')
# import smtplib
# server = smtplib.SMTP(smtp_server,25)
# server.set_debuglevel(1)
# server.login(from_addr,password)
# server.sendmail(from_addr,[to_addr],msg.as_string())
# server.quit()
    


    