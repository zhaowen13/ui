#coding=utf-8
from xml.dom.minidom import parse
import xml.dom.minidom
import Locator


class AnalyzeXml(object):
    map=''
    def Analyze(self,name,pagename):     #读取 xml 指定文件名和要读的page
        DOMTree = xml.dom.minidom.parse("./{0}.xml".format(name))
        collection = DOMTree.documentElement
        pages = collection.getElementsByTagName("page")
        table = {}         
        map=dict([(v,k) for k, v in table.iteritems()])     
        for page in pages:
            if page.getAttribute("pageName")==pagename:
                for locator in page.getElementsByTagName('locator'):
                    value=locator.getAttribute("value")
                    timeOut=locator.getAttribute("timeOut")
                    name=locator.childNodes[0].data
                    l = Locator.locator(name,timeOut,value)
                    map[locator.childNodes[0].data]=l
        return map         

if __name__ == '__main__':
    b = AnalyzeXml()
    m=b.Analyze('baidu','soso')
    print m[u'搜索'].value
    
