#coding=utf-8
import logging
import os
import ctypes
import time

global logger
class mylogs:

  @staticmethod
  def log():
    isExists=os.path.exists("./logs\\")
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs("./logs\\")
        print u'创建logs目录'
    global logger
    logger = logging.getLogger("./logs\\log.log")
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
    sh = logging.StreamHandler()
    sh.setFormatter(fmt)  # 设置CMD日志
    sh.setLevel(logging.INFO)
    fh = logging.FileHandler(filename='./logs\\log.log',
                            encoding='utf-8')  # 设置文件日志
    fh.setFormatter(fmt)
    fh.setLevel(logging.INFO)
    logger.addHandler(sh)
    logger.addHandler(fh)
  @staticmethod
  def debug(message):
    logger.debug(message)

  @staticmethod
  def info(message):
    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(message)
    # print('[{0}][INFO]{1}  '.format(time1,message))
    print('['+time1+']'+'[INFO]'+message+'  '.format())
   
  @staticmethod
  def war(message):
    logger.warn(message)

  @staticmethod
  def error(message):
    time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    logger.error(message)
    # print('[{0}][ERROR]{1}  '.format(time1,message))
    print('['+time1+']'+'[ERROR]'+message+'  ')

  @staticmethod
  def cri(message):
    logger.critical(message)
 
if __name__ =='__main__':
 mylogs.log()
 mylogs.debug(u'一个debug信息')
 mylogs.info(u'一个info信息')
 mylogs.war(u'一个warning信息')
 mylogs.error(u'一个error信息')
 mylogs.cri(u'一个致命critical信息')
