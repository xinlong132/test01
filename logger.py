# -*- coding: utf-8 -*-
"""
  ---------------------------
  @File: logger.py
  @Author: zyt
  @Date: 2017/10/26 15:24
  @Software: Pycharm
  @Version: Python2.7
  ---------------------------
"""

import logging
import os.path
import time


class Logger(object):

    def __init__(self,logger):
        """
        指定保存日志的路径，日志级别以及文件调用
        :param logger:
        :return:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler,用于写入日志文件
        Nowtime = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        log_path = os.getcwd()+'\\logs\\'
        log_name = log_path + Nowtime + '.log'
        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)-30s [line:%(lineno)-3d] [%(levelname)s] %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger