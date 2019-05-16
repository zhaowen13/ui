#coding=utf-8
import urllib2,sys
import json
from testcass import testcass

class cassjson(object):

    # def __init__(self):
    #     pass
    def Analyze(self,name):
        f = open("./cass\\{0}.json".format(name))  
        setting = json.load(f)
        list=[]
        se= setting[name]
        for colour in se: 
            type = colour['type']
            name=''
            text=''
            try:               
                name = colour['name'] 
                text=colour['text']
            except KeyError :
               pass             
            l = testcass(type,name,text)
            list.append(l)
        return list
if __name__ == '__main__':
    a=cassjson()
    print a.Analyze('login')[1]