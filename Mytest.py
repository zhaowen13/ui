#coding=utf-8
import HTMLTestRunner        
import unittest
from utils.mylogs import mylogs
from BasePage import BasePage

class MyTest(unittest.TestCase):#继承unittest.TestCase
    def myassertIs(self,member, container,BasePage,name):
        try:
            self.assertIs(member,container)
        except AssertionError as msg:
            mylogs.error(u"断言失败{0}".format(str(msg).encode('latin-1').decode('unicode_escape')))
            BasePage.Screenshot(name)
            BasePage.quit()
            raise
