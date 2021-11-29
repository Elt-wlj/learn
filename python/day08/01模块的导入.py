# 使用import 模块名
# 模块名也可以是文件名
# 1、引入内置模块
# 2、引入自定义模块

import random # 随机数模块
a = random.Random()# 范围是（0-1）之间的浮点数

# 2、引入自定义模块
import test
print(test.add(10,20))

# 3、引入模块中的函数
from test import add
print(test.add(10,20))

# 4、引入所有函数 import 文件名 import * ，我可以通过包中的__init__.py文件来自控制模块的导入
