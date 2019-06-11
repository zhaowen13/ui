# -*- coding:utf-8 -*-
import os
import yaml

class user(object):

    def getuser(self,name):
        yaml.load('../case/user.yaml', Loader=yaml.BaseLoader)
        yaml.warnings({'YAMLLoadWarning': False})
        with open('../case/user.yaml', 'r') as f:
            temp = yaml.load(f.read())
            users=temp[name]
            # for user in temp[name]:
            #     for username,password in user.items():
            #         print (username)
            #         print (password)
                # print password
        return users

if __name__ == "__main__":
    u=user()
    users=u.getuser('url')   
    print users['yingji']
            