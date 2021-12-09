# 元素定位
# 所有的ui层的自动化都是基于元素定位来实现的
# 所有的被操作的元素，都是webElement对象
# 元素 = HTML格式

# 标签：
# a:超链接
# img:图片
# input上传文件


from typing import Text
from selenium import webdriver
# 打开浏览器
driver = webdriver.Chrome()

# 八种元素定位：
# 1、id
# Name
# 2、link Text  超文本
# 3、parital link Text  like % 模糊匹配
# dr = driver.find_element_by_partial_link_text('百度')
# 当有多个模糊查询时，用 elements
# for d in dr :
#     print(d.text)
# +s 就是匹配多个
# 当模糊查询匹配到多个符合

# 4、classname 基于元素样式来进行定位
# 5、tagname 标签名进行定位----适用于重复率高
# driver.find_elements_by_tag_name('a')

# 6、xpath 路径定位，基于页面结构进行定位
# 绝对路径：从根/开始
# 相对路径：从当前开始，依照语法结构
# eg://*[@id ="kw"]

# //  表示根开始查找
# * 任意元素
# []表示筛选条件
# @ 表示基于属性来筛选,表示基于id属性值为kw的条件来进行筛选

'''
//button[@type='button']
//a[text()="登录"]
确认xpath是否正确：
    1、在开发者工具elements页面使用ctrl+f查找，进行判断
    2、在console中输入$x()进项校验
如果基于文本text来定位元素
在【】中添加text()='文本内容' 如：//a[text()="登录"]  //input[@value="百度一下"]
-------------
属性和文本不一样

当定位元素，无法直接定位时，可以通过子级元素返回父级来获取元素
//em[text()="阿斯达大"]/..  注意：要写你在输入框中写的内容

动态元素，也可以用想多路径，在用/..也可以返回上一级菜单

//input[@id="kw"]  等同于   //input[contains(@id,'kw')] 
contains表示进一步查找，匹配想模糊查找
//input[contains(text().'搜索')]

'''

# driver.find_element_by_xpath('')

# 7、cssselector css的选择器，应用相对较多的一种行为。基于class属性来实现的
# driver.find_element_by_css_selector('')


 