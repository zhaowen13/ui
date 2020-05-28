# --coding:utf-8--

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By 
from selenium.webdriver import Remote
from selenium.webdriver.common.action_chains import ActionChains
import time,os,random,sys
sys.path.append('..')
from utils.AnalyzeJson import AnalyzeJson
from utils.custom_logger import logger_cls
from utils.user import user



class BasePage(object):
    def __init__(self):
        self.driver=''
        self.loc=''
        self.myurl=''
        self.u=user()


    def open(self,browser,host='http://localhost:8081/wd/hub'):   # 初始化 打开浏览器 并最大化  self 与java中的this中一样，调用时不用传入self参数 
        try:
            self.driver = Remote(command_executor = host,
                            desired_capabilities = {'platform': 'ANY',
                                                    'browserName': browser,
                                                    'version': '',
                                                    'javascriptEnabled': True
                                                    }
                            )
            self.driver.maximize_window()
        except Exception as e:
            print(e)
        
        logger_cls.info(u"打开{0}浏览器".format(browser))              
        logger_cls.info(u"最大化")  
        

    def get(self,name):
        urls=self.u.getuser('url')
        url=urls[name]
        try:  
            self.driver.get(url)
            self.driver.implicitly_wait(10) # 隐性等待，最长等10秒    
            logger_cls.info(u'打开:{0}'.format(url))  
            self.myurl=url
        except BaseException:
            logger_cls.error(u'打开{0}失败'.format(url)) 
        self.loc=AnalyzeJson().Analyze(name)    #初始化，读取xml 赋值给loc
            
    def find(self,name):                 #元素定位，并返回定位好的元素
        try:
            el = WebDriverWait(self.driver,3,0.5).until(    #设置显示等待时间，每0.5秒检查一次，如果超出指定值就报错
            EC.presence_of_element_located((self.loc[name].type, self.loc[name].UIIdentifier)))
            logger_cls.info(u'定位元素:{0}'.format(name))
            # logger_cls.info(loc[name].value)
        except BaseException:
            logger_cls.error(u'定位元素:{0}失败'.format(name)) 
        return el

    def send_keys(self,name, text):
        try:
            self.find(name).send_keys(text) 
            logger_cls.info(u'在:{0}输入{1}'.format(name,text))
            time.sleep(3)
        except BaseException:
            logger_cls.error(u'在：{0}输入{1}失败'.format(name,text))

    def click(self,name):
        try: 
            self.find(name).click()
            logger_cls.info(u'点击:{0}'.format(name))
            time.sleep(3)
        except BaseException:
            logger_cls.error(u'点击:{0}失败'.format(name))
    
    def being(self,name):
        t=False
        try:
            self.driver.find_element_by_xpath(self.loc[name].UIIdentifier)
            t=True
            logger_cls.info(u'{0}元素存在'.format(name))
        except BaseException:
            logger_cls.info(u'{0}元素不存在'.format(name))
        return t

    def login(self,username,password):
        self.get(sys.argv[2])
        self.send_keys(u'用户名',username)
        self.send_keys(u'密码',password)
        self.click(u'登录')
        time.sleep(3)
        if  self.get_url()!=self.myurl:
            logger_cls.info(u"登录成功")
        else:
            logger_cls.error(u"登录失败")
        if self.being(u'不再提示'):
            self.click(u'不再提示')
        self.get_version()
    
    def clearmonitor(self):
        names=[u'博主',u'博主圈']
        self.click(u'事件') 
        if self.being(u'是否有事件'):
                self.focus(u'找回')
                self.click(u'多选')
                self.click(u'全选')
                self.click(u'删除')
        for name in names:
            self.click(name) 
            if self.being(u'是否有博主'):
                self.focus(u'找回')
                self.click(u'多选')
                self.click(u'全选')
                self.click(u'删除')            
       


    def randomclick(self,name,div=None):
        text=''
        i=len(self.driver.find_elements_by_xpath(self.loc[name].UIIdentifier))
        logger_cls.info(u'{0}列表中有{1}个参数'.format(name,i))
        y=random.randint(1, i)
        if div==None:
            path=self.loc[name].UIIdentifier+'['+str(y)+']'
            text=self.driver.find_element_by_xpath(path).text
            self.driver.find_element_by_xpath(path).click()
            logger_cls.info(u'随机选择列表中的{0}第个参数并点击'.format(y))
        else:
            i2=len(self.driver.find_elements_by_xpath(self.loc[name].UIIdentifier+'['+str(y)+']'))
            y2=random.randint(1, i2)
            path=self.loc[name].UIIdentifier+'['+str(y2)+']'+div
            text=self.driver.find_element_by_xpath(path).text
            self.driver.find_element_by_xpath(path).click()
            logger_cls.info(u'随机选择列表中的{0}第个参数并点击'.format(y2))  
      
        logger_cls.info(u'{0}:文本的值为:{1}'.format(name,text))
        time.sleep(3)
        return text
        
    

    def close(self):
        logger_cls.info(u'3秒后关闭当前页面')
        time.sleep(3)
        self.driver.close()

    def quit(self):
        logger_cls.info(u'3秒后关闭浏览器')
        time.sleep(3)
        self.driver.quit()

    def get_url(self):
        url=self.driver.current_url  
        logger_cls.info(u'当前页面url:'+url)    
        return url

    def get_text(self,name):
        text=self.find(name).text
        logger_cls.info(u'{0}文本框的值为:{1}'.format(name,text))
        return text

    def back(self):   
        self.driver.back()
        logger_cls.info(u'返回上一页面')

    def clear(self,name):
        self.find(name).clear()  
        logger_cls.info(u'清空文本框:{0}'.format(name)) 

    def get_name(self):
        name=self.driver.name
        logger_cls.info(u'浏览器名称：{0}'.format(name))

    def get_driver(self):
        return self.driver

    def get_version(self):
        version=self.driver.capabilities['version'] 
        logger_cls.info(u'浏览器版本：{0}'.format(version))
        return version

    def switch_to(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        logger_cls.info(u'切换页面')


    def focus(self,name):
        ele = self.find(name)
        ActionChains(self.driver).move_to_element(ele).perform()
        logger_cls.info(u'鼠标悬停到元素:{0}'.format(name))

    def refresh(self):
        self.driver.refresh()
        logger_cls.info(u'刷新页面')

    def title(self):
        title=self.driver.title
        logger_cls.info(u'当前页面标题'+title)    
        return title
    
    def Slide(self,height):
        js="var q=document.documentElement.scrollTop={0}".format(str(height))
        self.driver.execute_script(js)
        logger_cls.info(u'上下滑动'+str(height))

    def sleep(self,i):
        logger_cls.info(u'暂停{0}秒'.format(i))
        time.sleep(int(i))

    def Screenshot(self,name):
        # name='screenshot_'
        isExists=os.path.exists("../images\\")
        # 判断结果
        if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
            os.makedirs("../images\\")
            print u'创建images目录'
        timestrmap = time.strftime('%Y%m%d_%H%M%S')
        imgPath = os.path.join('../images\\', str(timestrmap)+name+'.png')
        self.driver.save_screenshot(imgPath)
        logger_cls.info(u'截图:{0}{1}.png'.format(str(timestrmap),name))
       
   

if __name__ == "__main__":
    t = BasePage()
    # t.open("https://www.eagtek.com/eagtek/login")
    # t.login("systemtest07","g7SdT*")
    # time.sleep(6)
    # t.click(u'搜索')
    # t.myrandom(u'监测事件')
    # print t.getCount(u'范围')
    # t.click(u'百度一下')
    # t.Screenshot(u'百度')
    # time.sleep(3)
    # # t.back()
    # t.click(u'百度翻译')
    # time.sleep(3)
    # t.switch_to()
    # t.Slide(500)
    # time.sleep(3)
    # t.Slide(-500)
    # t.refresh()
    # t.get_url()
    # t.get_version() 
    # t.quit()
      
