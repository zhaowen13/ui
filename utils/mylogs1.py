#coding=utf-8
import logging
import os
import time
 
class mylogs(object):
    def __init__(self, path):
        self.path='../logs\\'+path+'.log'
        isExists=os.path.exists("../logs\\")
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs("../logs\\")
            print u'创建logs目录'
        self.logger = logging.getLogger(self.path)
        self.logger.setLevel(logging.INFO)
        self.fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        #设置CMD日志
        sh = logging.StreamHandler()
        sh.setFormatter(self.fmt)
        sh.setLevel(logging.INFO)
        #设置文件日志
        self.fh = logging.FileHandler(self.path)
        self.fh.setFormatter(self.fmt)
        self.fh.setLevel(logging.INFO)
        self.logger.addHandler(sh)
        self.logger.addHandler(self.fh)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        time1 = time.strftime('%Y-%m-%d %H:%M:%S')
        self.logger.info(message)
        # print('['+time1+']'+'[INFO]'+message)

    def war(self,message):
        self.logger.warn(message)

    def error(self,message):
        time1 = time.strftime('%Y-%m-%d %H:%M:%S')
        self.logger.error(message)
        # print('['+time1+']'+'[ERROR]'+message)

    def cri(self,message):
        self.logger.critical(message)
 
if __name__ =='__main__':
    logyyx = mylogs(u'log.log')
    logyyx.debug(u'一个debug信息')
    logyyx.info(u'一个info信息')
    logyyx.war(u'一个warning信息')
    logyyx.error(u'一个error信息')
    logyyx.cri(u'一个致命critical信息')