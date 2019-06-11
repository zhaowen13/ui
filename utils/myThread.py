
#!/usr/bin/python
#coding=utf-8
 
import threading
import time
 
exitFlag = 0
 
class myThread (threading.Thread):   
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):                  
       pass

if __name__ == "__main__":
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    # 开启线程
    thread1.start()
    thread2.start()
 

 


 

