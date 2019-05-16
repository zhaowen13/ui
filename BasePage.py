# --coding:utf-8--

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
import time,os
from utls.AnalyzeJson import AnalyzeJson
from utls.mylogs import mylogs


global driver
loc=''
class BasePage(object):
    def __init__(self,type,name):   # 初始化 打开浏览器 并最大化  self 与java中的this中一样，调用时不用传入self参数
        self.type=type
        if type == "Google":
            global driver           
            driver=webdriver.Chrome()
            mylogs.info(u"打开谷歌浏览器")  
        elif type == "firefox":
            driver=webdriver.Firefox()
            mylogs.info(u"打开火狐浏览器")  
        driver.maximize_window()  
        mylogs.info(u"最大化") 
        global loc     
        loc=AnalyzeJson().Analyze(name)    #初始化，读取xml 赋值给loc

    def open(self,url):
        try:  
            driver.get(url)
            driver.implicitly_wait(10) # 隐性等待，最长等10秒    
            mylogs.info(u'打开:{0}'.format(url))  
        except BaseException:
            mylogs.error(u'打开{0}失败'.format(url)) 
            
    def find(self,name):                 #元素定位，并返回定位好的元素
        try:
            el = WebDriverWait(driver,3,0.5).until(    #设置显示等待时间，每0.5秒检查一次，如果超出指定值就报错
            EC.presence_of_element_located((By.XPATH, loc[name].UIIdentifier)))
            mylogs.info(u'定位元素:{0}'.format(name))
            # mylogs.info(loc[name].value)
        except BaseException:
            mylogs.error(u'定位元素{0}失败'.format(name)) 
        return el

    def send_keys(self,name, text):
        try:
            self.find(name).send_keys(text) 
            mylogs.info(u'在:{0}输入{1}'.format(name,text))
            time.sleep(3)
        except BaseException:
            mylogs.error(u'在：{0}输入{1}失败'.format(name,text))

    def click(self,name):
        try: 
            self.find(name).click()
            mylogs.info(u'点击{0}'.format(name)) 
        except BaseException:
            mylogs.error(u'点击：{0}失败'.format(name))
     
    def close(self):
        mylogs.info(u'3秒后关闭当前页面')
        time.sleep(3)
        driver.close()

    def quit(self):
        mylogs.info(u'3秒后关闭浏览器')
        time.sleep(3)
        driver.quit()

    def get_url(self):
        url=driver.current_url  
        mylogs.info(u'当前页面url:'+url)    
        return url

    def get_text(self,name):
        text=self.find(name).is_enabled()
        mylogs.info(u'{0}文本框的值为：'.format(text))

    def back(self):   
        driver.back()
        mylogs.info(u'返回上一页面')

    def clear(self,name):
        self.find(name).clear()  
        mylogs.info(u'清空文本框:{0}'.format(name)) 

    def get_name(self):
        name=driver.name
        mylogs.info(u'浏览器名称：{0}'.format(name))

    def get_driver(self):
        return driver

    def get_version(self):
        version=driver.capabilities['version'] 
        mylogs.info(u'浏览器版本：{0}'.format(version))
        return version

    def switch_to(self):
        driver.switch_to.window(driver.window_handles[-1])
        mylogs.info(u'切换页面')


    def refresh(self):
        driver.refresh()
        mylogs.info(u'刷新页面')

    def title(self):
        title=driver.title
        mylogs.info(u'当前页面标题'+title)    
        return title
    
    def Slide(self,height):
        js="var q=document.documentElement.scrollTop={0}".format(str(height))
        driver.execute_script(js)
        mylogs.info(u'上下滑动'+str(height))

    def sleep(self,i):
        mylogs.info(u'暂停{0}秒'.format(i))
        time.sleep(int(i))

    def Screenshot(self,name):
        isExists=os.path.exists("./images\\")
        # 判断结果
        if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
            os.makedirs("./images\\")
            print u'创建images目录'
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join('./images\\', name+str(timestrmap)+'.png')
        driver.save_screenshot(imgPath)
        mylogs.info(u'截图:{0}{1}.png'.format(name,str(timestrmap)))
       
   

if __name__ == "__main__":
    mylogs.log()
    t = BasePage("Google",'locators')
    t.open("https://www.baidu.com")
    t.send_keys(u"搜索","test")
    time.sleep(3)
    t.click(u'百度一下')
    t.Screenshot(u'百度')
    time.sleep(3)
    # t.back()
    t.click(u'百度翻译')
    time.sleep(3)
    t.switch_to()
    t.Slide(500)
    time.sleep(3)
    t.Slide(-500)
    t.refresh()
    t.get_url()
    t.get_version() 
    t.quit()
      
