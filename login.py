#coding=utf-8
import HTMLTestRunner        
import unittest
from utils.mylogs import mylogs
from Mytest import MyTest
from action import action
from utils.Context import context

class login(MyTest):#继承unittest.TestCase
    def test_run2(self):
        a=action()
        a.go('login2')
        self.myassertIs(context.get("member"),context.get("container"),context.get("driver"),context.get("name"))
        #测试用例
    def test_run3(self):
        # self.assertEqual(1,1)
        self.assertIs(1,1)
        #测试用例
    def test_run1(self):
        a=action()
        a.go('login')
        
# self.myassertIs(1,2,t,u'百度一下')
    

if __name__ == '__main__':
    mylogs.log()
    test_suite = unittest.TestSuite()#创建一个测试集合
    test_suite.addTest(login('test_run1'))#测试套件中添加测试用例
    test_suite.addTest(login('test_run2'))#测试套件中添加测试用例
    #test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    fp = open('res.html','wb')#打开一个保存结果的html文件
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'UI测试报告',description=u'测试情况')
    #生成执行用例的对象
    runner.run(test_suite)
    #执行测试套件
