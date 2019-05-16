#coding=utf-8
import urllib2
import json
from Locator import locator


class AnalyzeJson(object):   

    def Analyze(self,name):
        f = open("./loc\\{0}.json".format(name))  
        setting = json.load(f)
        table = {}         
        map=dict([(v,k) for k, v in table.iteritems()])    
        for colour in setting:
            name = colour['name']
            UIIdentifier = colour['UIIdentifier'] 
            type=colour['type']
            l = locator(name,type,UIIdentifier)
            map[name]=l    
        return map
if __name__ == '__main__':
    a=AnalyzeJson()
    a.Analyze('')