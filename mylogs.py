#coding=utf-8
import logging
import os
import ctypes
import time

class mylogs:


  def __init__(self):
    isExists=os.path.exists("./logs\\")
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs("./logs\\")
        print u'创建logs目录'
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
    print(message)

  def info(self,message):
    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    self.logger.info(message)
    # print("<pre style=\"color:Green:scroll; overflow-x:hidden;height:200px; width:600px; margin:auto; border:1px solid #e1e1e1;\">测试一下</pre>")
    print(time1+'[info]'+message)

  def war(self,message):
    self.logger.warn(message)
    print(message)

  def error(self,message):
    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    self.logger.error(message)
    print(time1+'[error]'+message)

  def cri(self,message):
    self.logger.critical(message)
    print(message)
 
if __name__ =='__main__':
 logyyx = mylogs()
 logyyx.debug(u'一个debug信息')
 logyyx.info(u'一个info信息')
 logyyx.war(u'一个warning信息')
 logyyx.error(u'一个error信息')
 logyyx.cri(u'一个致命critical信息')
