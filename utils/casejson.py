#coding=utf-8
import urllib2,sys
import json
from testcase import testcase

class casejson(object):

    # def __init__(self):
    #     pass
    def Analyze(self,name):
        f=''
        if name=='login':
            f = open("../case\\"+name+".json") 
        else:
            f= open('../case\\'+sys.argv[2]+'\\'+name+'.json')
        setting = json.load(f)
        list=[]
        # se= setting[name]
        for colour in setting: 
            type = colour['type']
            name=''
            text=''
            try:               
                name = colour['name'] 
                text=colour['text']
            except KeyError :
               pass             
            l = testcase(type,name,text)
            list.append(l)
        return list
if __name__ == '__main__':
    a=casejson()
    list =a.Analyze(u'事件监测列操作')
    for i in list:
        print i.name
