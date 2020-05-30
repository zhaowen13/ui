# -*- coding: utf-8 -*-
import sys,time
sys.path.append('..')
from action.BasePage import BasePage

t= BasePage("yingji")

class theme(object):
    def login(slef):
        t.open()
        t.login()
        time.sleep(6)
        t.quit()
        return u"区域用户"