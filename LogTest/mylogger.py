import logging
from logging import Formatter, Logger
from myconf import MyConf

class MyLogger(Logger):
    def __init__(self):
        conf = MyConf('conf.ini')
        super().__init__(conf.get('log','name'),conf.get('log','level'))
        # 日志类格式化
        fmt_str = "%(asctime)s %(name)s %(levelname)s %(filename)s [%(lineno)d] %(message)s"
        # 实例化日志类
        formatter  = logging.Formatter(fmt_str)
        # 输出到控制台
        handle = logging.StreamHandler(formatter)
        # 绑定渠道
        handle.addFilter(handle)
logger = MyLogger()