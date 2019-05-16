#coding=utf-8
class locator(object):
    def __init__(self,name,type,UIIdentifier):
       self.name=name                #元素名称
       self.type=type          #定位方式
       self.UIIdentifier=UIIdentifier              #定位信息
if __name__ == '__main__':
    b = locator('wenzhao','10000','sdffdsf')
    print b.name
    # print b.get_value().decode('utf-8').encode('cp936')  
    # b.deom_add_test('test')
    

        
