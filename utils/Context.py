#coding=utf-8

table={}     
map=dict([(v,k) for k, v in table.iteritems()])

class context(object):
    
    @staticmethod
    def set(key,value):             
        map[key]=value

    @staticmethod   
    def get(key):
        return map[key]

if __name__ == "__main__":
    context.set("zhao","wen")
    print context.get("zhao")
   