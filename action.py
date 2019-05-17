#coding=utf-8
import urllib2,sys
from BasePage import BasePage
from utils.cassjson import cassjson
from utils.mylogs import mylogs

class action(object):
    
    def go(self,name):
        c=cassjson()
        list=c.Analyze(name)
        for i in list:
                if i.type==u'打开浏览器':
                    global driver
                    driver=BasePage(i.name,i.text)
                elif i.type==u'打开页面':
                    driver.open(i.name)
                elif i.type==u'点击':
                    driver.click(i.name)
                elif i.type==u'输入':
                    driver.send_keys(i.name,i.text)
                elif i.type==u'切换页面':
                    driver.switch_to()
                elif i.type==u'暂停':
                    driver.sleep(i.name)
                elif i.type==u'关闭页面':
                    driver.close()
                elif i.type==u'关闭浏览器':
                    driver.quit()
                elif i.type==u'url':
                    driver.get_url()
                elif i.type==u'文本框的值':
                    driver.get_text()
                elif i.type==u'返回上一页面':
                    driver.back()
                elif i.type==u'清空文本框':
                    driver.clear()
                elif i.type==u'浏览器名称':
                    driver.get_name()
                elif i.type==u'浏览器版本':
                    driver.get_version()
                elif i.type==u'刷新页面':
                    driver.refresh()
                elif i.type==u'页面标题':
                    driver.title()
                elif i.type==u'上下滑动':
                    driver.Slide(i.name)
if __name__ == "__main__":
    mylogs.log()
    a=action()
    a.go('login')
    pass
