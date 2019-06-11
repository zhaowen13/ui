# coding=utf-8
import os,sys
import yaml
from testcase import testcase

class caseyaml(object):

    def Analyze(self,name):
        if name!='login':
            name=sys.argv[2]+'\\'+name
        yaml.load(u'../case/{0}.yaml'.format(name), Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        list=[]
        with open(u'../case/{0}.yaml'.format(name), 'r') as f:
            temp = yaml.load(f.read())
            for case in temp:
                type = case['type']
                name=''
                text=''
                try:               
                    name = case['name'] 
                    text=case['text']
                except KeyError :
                    pass             
                l = testcase(type,name,text)
                list.append(l)          
        return list

if __name__ == "__main__":
    u=caseyaml()
    users=u.getuser('test')   
    for u in users:
        print u.type
        print u.name
        print u.text