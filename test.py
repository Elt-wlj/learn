import re  # 正则表达式，用于文字匹配
from bs4 import BeautifulSoup  # 用于网页解析，对HTML进行拆分，方便获取数据
import urllib.request, urllib.error, urllib.parse  # 用于指定URL，给网址就能进行爬取
import xlwt  # 用于Excel操作
import sqlite3  # 用于进行SQLite数据库操作
import ssl

# 正则表达式：.表示任意字符，*表示0次或任意次，？表示0次或1次。（.*?)惰性匹配。
findLink = re.compile(r'<a href="(.*?)">')  # 获取电影详情链接。
findImg = re.compile(r'<img.*src="(.*?)"', re.S)  # 获取影片图片。re.S 让换行符包含在字符串中
findTitle = re.compile(r'<span class="title">(.*)</span>')  # 获取影片名称(可能有两个)
findOther = re.compile(r'<span class="other">(.*)</span>')  # 获取影片别称（多个别称以\分割）
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 获取影片评分
findJudge = re.compile(r'<span>(\d*)人评价</span>')  # 获取评价人数
findInq = re.compile(r'<span class="inq">(.*)</span>')  # 获取影片概括
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)  # 获取影片相关内容


def main():
    # 处理SSL
    ssl._create_default_https_context = ssl._create_unverified_context

    # 豆瓣Top250网址(末尾的参数 ?start= 加不加都可以访问到第一页)
    baseUrl = "https://movie.douban.com/top250?start="
    # 1. 爬取网页并解析数据
    dataList = getData(baseUrl)
    # 2. 保存数据
    dbPath = "movie.db"
    saveDataToDB(dataList, dbPath)  # SQLite


# 得到一个指定URL的网页内容
def askURL(url):
    # 模拟头部信息，像豆瓣服务器发送消息
    # User-Agent 表明这是一个浏览器（这个来自F12里Network中 Request headers的User-Agent）
    head = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    # 封装头部信息
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        # 发起请求并获取响应
        response = urllib.request.urlopen(request)
        # 读取整个HTML源码，并解码为UTF-8
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        # 异常捕获
        if hasattr(e, "code"):
            print("状态码：", e.code)
        if hasattr(e, "reason"):
            print("原因：", e.reason)
    return html


# 爬取网页，返回数据列表
def getData(baseurl):
    dataList = []
    # 爬取所有网页并获取需要的HTML源码
    for i in range(0, 1):  # 豆瓣Top250 共有10页，每页25条。 range(0,10)的范围是[0,10)。
        url = baseurl + str(i * 1)  # 最终 url = https://movie.douban.com/top250?start=225
        html = askURL(url)  # 将每个页面HTML源码获取出来
        # 对页面源码逐一解析
        soup = BeautifulSoup(html, "html.parser")  # 设置解析器
        for item in soup.find_all("div", class_="item"):  # 查找 class为item的div标签
            data = []  # 保存一部电影数据（每部电影由<div class="item">划分）
            item = str(item)  # 把item转为字符串类型(原本是Tag类型对象)

            # findall返回匹配成功的列表。
            link = re.findall(findLink, item)[0]  # 获取影片详情页链接，只需要一个就行。这里会返回两个。
            data.append(link)  # 把link追加到data里

            img = re.findall(findImg, item)[0]  # 获取影片图片链接
            data.append(img)

            titles = re.findall(findTitle, item)  # 获取影片名称
            # 有的影片title是两个，有的是一个。如果只有一个，则第二个保存空。
            if (len(titles) == 2):
                data.append(titles[0])  # 中文名称
                titles[1] = re.sub("(/)|( )", " ", titles[1])
                data.append("".join(titles[1].split()))  # 英文名称
            else:
                data.append(titles[0])  # 中文名称
                data.append("")  # 没有英文名称，添加空

            other = re.findall(findOther, item)[0]  # 获取影片别称
            other = other.replace("/", "", 1)
            other = re.sub("(&nbsp;)|(NBSP)|(\\xa0)|( )", "", other)
            data.append(other)

            rating = re.findall(findRating, item)[0]  # 获取影片评分
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]  # 获取影片评论人数
            data.append(judgeNum)

            inq = re.findall(findInq, item)  # 获取影片概述(可能不存在)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")  # 去掉句号
                data.append(inq)
            else:
                data.append("")

            bd = re.findall(findBd, item)[0]  # 获取影片相关（删除不想要的符号）
            bd = re.sub('\\xa0', "  ", bd)  # 去除 HTML 空格符 &nbsp;
            bd = re.sub('(/\.\.\.)|(<br/>)|<br>', " ", bd)
            bd = re.sub("(    )|(\n)", "", bd)
            data.append(bd.strip())  # strip 去掉前后空格

            dataList.append(data)
    # 返回解析好的数据
    return dataList

# 初始化数据库
def iniDB(dbPath):
    print("正在初始化...")
    # 创建表
    sql = '''
        create table if not exists movie250(
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            c_name varchar,
            e_name varchar,
            other_name varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
        );
    '''
    connect = sqlite3.connect(dbPath)
    cursor = connect.cursor()
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
    print("初始化完成！！")


# 保存数据(SQLite)
def saveDataToDB(dataList, dbPath):
    iniDB(dbPath)  # 初始化数据库
    connect = sqlite3.connect(dbPath)
    cursor = connect.cursor()

    print("正在入库...")
    # dataList存储了250部电影的信息，data一部电影的信息列表，它包含了9个元素。
    for data in dataList:
        # 这个for循环是为了将列表字符串元素都加上双引号，因为后面拼接sql时 每个元素需要双引号括起来。
        for index in range(len(data)):
            # 下标6和7的元素是score和rated，是数字类型，不需要引号。
            if index == 5 or index == 6:
                continue
            data[index] = '"' + data[index] + '"'
        # 下面是用 %s 作为占位符，填充的是 ",".join(data)。
        # ",".join(data)表明 把列表data转为字符串且每个元素用逗号隔开。
        sql = '''
            insert into movie250(
            info_link, pic_link, c_name, e_name, other_name, score, rated, introduction, info)
            values(%s)''' % ",".join(data)
        cursor.execute(sql)
        connect.commit()
    cursor.close()
    connect.close()
    print("入库完毕!!")


# 程序入口
if __name__ == "__main__":
    main()
