#coding=utf-8      
import unittest,sys
from utils.custom_logger import logger_cls
from Context import context
sys.path.append('..')
from action.BasePage import BasePage



class MyTest(unittest.TestCase):#继承unittest.TestCase
    def myassertIs(self):
        member=context.get("member")
        container=context.get("container")
        driver=context.get("driver")
        name=context.get("name")
        try:
            self.assertIs(member,container)
            logger_cls.info(u"断言成功:{0}等于{1}".format(member,container))
        except AssertionError:
            logger_cls.error(u"断言失败:{0}不等于{1}".format(member,container))
            driver.Screenshot(name)
            # driver.quit()
            raise

    def myassertIn(self):
        logger_cls.info(u'进入断言')
        member=context.get("member")
        container=context.get("container")
        driver=context.get("driver")
        name=context.get("name")
        try:
            self.assertIn(member,container)
            logger_cls.info(u"断言成功:{0}包含{1}".format(member,container))
        except AssertionError:
            logger_cls.error(u"断言失败:{0}不包含{1}".format(member,container))
            driver.Screenshot(name)
            raise