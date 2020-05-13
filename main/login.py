#coding=utf-8
from ExtentHTMLTestRunner  import HTMLTestRunner    
# from HTMLTestRunner  import HTMLTestRunner    
import unittest,sys
sys.path.append('..')
from utils.Mytest import MyTest
from action.action import action
from utils.Context import context
from utils.mylogs import mylogs
from utils.user import user


class login2(MyTest):#继承unittest.TestCase 
    u''':登录'''
    def test_run(self):
        u''':谷歌登录'''
        a=action()
        a.go('login')
        context.set('action',a)
    
    # def test_run2(self):
    #     u''':帐号设置'''
    #     a=context.get('action')
    #     a.go(u'帐号设置')

    def test_run3(self):
        # u''':偏好设置'''
        a=context.get('action')
        a.go(u'偏好设置') 
        self.myassertIn()   

if __name__ == "__main__":
    u=user()
    users=u.getuser(sys.argv[2])
    usernames=[]
    passwords=[] 
    for user in users:
        for username,password in user.items():
            usernames.append(username)
            passwords.append(password)  
    context.set('username',usernames[0])
    context.set('password',passwords[0]) 
    mylogs.log()
    test_suite = unittest.TestSuite()#创建一个测试集合
    test_suite.addTest(unittest.makeSuite(login2))#使用makeSuite方法添加所有的测试方法
    fp = open('../res.html','wb')#打开一个保存结果的html文件
    runner = HTMLTestRunner(stream=fp,title=u'UI测试报告',description=u'测试情况')
    runner.run(test_suite) #运行测试
    pass
    
   
