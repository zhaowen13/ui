
#coding=utf-8
 
import threading
import time
from ExtentHTMLTestRunner  import HTMLTestRunner    
import unittest,sys,os
sys.path.append('..')
from utils.mylogs import mylogs
from utils.user import user
from utils.Context import context
 
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, username, password):
        threading.Thread.__init__(self)
        self.username = username
        self.password = password
        
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数   
        context.set('username',self.username)
        context.set('password',self.password)
        isExists=os.path.exists("../report\\")
        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs("../report\\")
            print u'创建report目录'
        discover = unittest.defaultTestLoader.discover(sys.argv[2],
                                                    pattern='*.py',
                                                    top_level_dir=None)
        fp = open('../report\\{0}.html'.format(sys.argv[2]),'wb')#打开一个保存结果的html文件
        runner = HTMLTestRunner(stream=fp,title=sys.argv[2]+'UI测试报告',description=u'测试情况')
        runner.run(discover)
        

if __name__ == "__main__":
    mylogs.log()
    u=user()
    users=u.getuser(sys.argv[2])
    usernames=[]
    passwords=[]
    for user in users:
        for username,password in user.items():
            usernames.append(username)
            passwords.append(password)                                   
    thread1 = myThread(usernames[0], passwords[0])
    # thread2 = myThread(usernames[1], passwords[1],'yingji2')
    # 开启线程
    thread1.start()
    # time.sleep(3)
    # thread2.start()