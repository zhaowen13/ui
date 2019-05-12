# --coding:utf-8--

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
import time
import mylogs
import AnalyzeXml

global driver
log=mylogs.mylogs()     #文件名点类名  
loc=''
class test(object):
    def __init__(self,type,name,pagename):   # 初始化 打开浏览器 并最大化  self 与java中的this中一样，调用时不用传入self参数
        self.type=type
        if type == "Google":
            global driver           
            driver=webdriver.Chrome()
            log.info(u"打开谷歌浏览器")  
        elif type == "firefox":
            driver=webdriver.Firefox()
            log.info(u"打开火狐浏览器")  
        driver.maximize_window()  
        log.info(u"最大化") 
        global loc     
        loc=AnalyzeXml.AnalyzeXml().Analyze(name,pagename)    #初始化，读取xml 赋值给loc

    def open(self,url):
        try:  
            driver.get(url)
            driver.implicitly_wait(10) # 隐性等待，最长等10秒    
            log.info(u'打开:{0}'.format(url))  
        except BaseException:
            log.error(u'打开{0}失败'.format(url)) 
            
    def find(self,name):                 #元素定位，并返回定位好的元素
        try:
            el = WebDriverWait(driver,int(loc[name].timeOut),0.5).until(    #设置显示等待时间，每0.5秒检查一次，如果超出指定值就报错
            EC.presence_of_element_located((By.XPATH, loc[name].value)))
            log.info(u'定位元素:{0}'.format(name))
            # log.info(loc[name].value)
        except BaseException:
            log.error(u'定位元素{0}失败'.format(name)) 
        return el

    def send_keys(self,name, text):
        try:
            self.find(name).send_keys(text) 
            log.info(u'在:{0}输入{1}'.format(name,text))
            time.sleep(3)
        except BaseException:
            log.error(u'在：{0}输入{1}失败'.find(name,text))

    def click(self,name):
        try: 
            self.find(name).click()
            log.info(u'点击{0}'.format(name)) 
        except BaseException:
            log.error(u'点击：{0}失败'.find(name))
     
    def close(self):
        log.info(u'3秒后关闭当前页面')
        time.sleep(3)
        driver.close()

    def quit(self):
        log.info(u'3秒后关闭浏览器')
        time.sleep(3)
        driver.quit()

    def get_url(self):
        url=driver.current_url  
        log.info(u'当前页面url: {0}'.find(url))     
        return url

    def get_text(self,name):
        text=self.find(name).is_enabled()
        log.info(u'{0}文本框的值为：'.find(text))

    def back(self):   
        driver.back()
        log.info(u'返回上一页面')

    def clear(self,name):
        self.find(name).clear()  
        log.info(u'清空文本框{0}'.find(name)) 

    def get_name():
        name=driver.name
        log.info(u'浏览器名称： {0}'.find(name))

if __name__ == "__main__":
    t = test("Google",'baidu','soso')
    t.open("https://www.baidu.com")
    t.send_keys(u"搜索","test")
    t.click(u'百度一下')
    time.sleep(3)
    t.click(u'百度翻译')
    t.get_url()
    t.quit()
      