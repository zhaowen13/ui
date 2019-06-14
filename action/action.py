# coding=utf-8
import urllib2
import sys
from BasePage import BasePage
sys.path.append('..')
from utils.caseyaml import caseyaml
from utils.Context import context
from utils.mylogs import mylogs
from utils.Random import Random
from utils.user import user

class action(object):
    def __init__(self):
        self.driver=BasePage()
        self.username=context.get('username')
        self.password=context.get('password')
        context.set('email',Random().RandomEmail())
        context.set('phone',Random().Randomphone())


    def go(self, name):
        c = caseyaml()
        list = c.Analyze(name)
        for i in list:
            if i.type == u'打开浏览器':
                self.driver.open(sys.argv[1],sys.argv[3])       #指定远程机器
                #self.driver.open(sys.argv[1])    #在本地跑时
            elif i.type == u'打开页面':
                self.driver.get(i.name)
            elif i.type ==u'清空监测列':
                self.driver.clearmonitor()
            elif i.type == u'登录':   
                self.driver.login(self.username, self.password)
            elif i.type == u'点击':
                if '${' in i.name:
                    name = context.get(i.name.replace(
                        '$', ''))
                    self.driver.click(name)
                else:
                    self.driver.click(i.name)
            elif i.type == u'输入':
                if '$' in i.text:
                    text = context.get(i.text.replace(
                        '$', ''))
                    self.driver.send_keys(i.name,text)
                else:
                    self.driver.send_keys(i.name, i.text)
            elif i.type == u'切换页面':
                self.driver.switch_to()
            elif i.type == u'暂停':
                self.driver.sleep(i.name)
            elif i.type == u'随机选择列表中的值点击':
                text=self.driver.randomclick(i.name)
                context.set(i.name,text)
            elif i.type == u'随机选择列表中的值点击2':
                text=self.driver.randomclick(i.name,i.text)   
                context.set(i.name,text)         
            elif i.type == u'关闭页面':
                self.driver.close()
            elif i.type == u'关闭浏览器':
                self.driver.quit()
            elif i.type == u'url':
                self.driver.get_url()
            elif i.type == u'文本框的值':
                text = self.driver.get_text(i.name)
                context.set(i.name, text)
            elif i.type == u'返回上一页面':
                self.driver.back()
            elif i.type == u'清空文本框':
                self.driver.clear(i.name)
            elif i.type == u'浏览器名称':
                self.driver.get_name()
            elif i.type == u'浏览器版本':
                self.driver.get_version()
            elif i.type == u'刷新页面':
                self.driver.refresh()
            elif i.type == u'页面标题':
                self.driver.title()
            elif i.type == u'上下滑动':
                self.driver.Slide(i.name)
            elif i.type == u'断言':
                mylogs.info(u'要开始断言了')
                context.set("driver", self.driver)
                context.set("name", name)           #用例名称
                context.set("member", context.get(i.name))
                context.set("container", context.get(i.text))


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
    a = action()
    a.go('login')
    a.go(u'偏好设置')
    
    pass
