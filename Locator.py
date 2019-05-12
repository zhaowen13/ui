#coding=utf-8
class locator(object):
    def __init__(self,name,timeOut,value):
       self.name=name                #元素名称
       self.timeOut=timeOut          #定位超时时间
       self.value=value              #定位时间
if __name__ == '__main__':
    b = locator('wenzhao','10000','牛逼')
    print b.name
    # print b.get_value().decode('utf-8').encode('cp936')  
    # b.deom_add_test('test')
    

        
