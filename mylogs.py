#coding=utf-8
import logging
import os
import ctypes


class mylogs:


  def __init__(self):
    self.logger = logging.getLogger("./logs\\log.log")
    self.logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)  # 设置CMD日志
    sh.setLevel(logging.INFO)
    fh = logging.FileHandler(filename='./logs\\log.log',
                            encoding='utf-8')  # 设置文件日志
    fh.setFormatter(fmt)
    fh.setLevel(logging.INFO)
    self.logger.addHandler(sh)
    self.logger.addHandler(fh)

  def debug(self,message):
    self.logger.debug(message)

  def info(self,message):
    self.logger.info(message)

  def war(self,message):
    self.logger.warn(message)

  def error(self,message):
   self.logger.error(message)

  def cri(self,message):
    self.logger.critical(message)
 
if __name__ =='__main__':
 logyyx = mylogs()
 logyyx.debug(u'一个debug信息')
 logyyx.info(u'一个info信息')
 logyyx.war(u'一个warning信息')
 logyyx.error(u'一个error信息')
 logyyx.cri(u'一个致命critical信息')
