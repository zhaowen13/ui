# --coding:utf-8--
import random


class Random(object):

    def RandomEmail(self, emailType=None, rang=None):
        __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
        # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
        if emailType == None:
            __randomEmail = random.choice(__emailtype)
        else:
            __randomEmail = emailType
        # 如果没有指定邮箱长度，默认在4-10之间随机
        if rang == None:
            __rang = random.randint(4, 10)
        else:
            __rang = int(rang)
        __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        __randomNumber = "".join(random.choice(__Number)
                                 for i in range(__rang))
        _email = __randomNumber + __randomEmail
        return _email

    def Randomphone(self):
        second = [3, 4, 5, 7, 8][random.randint(0, 4)] # 第三位数字 
        third = {
        3: random.randint(0, 9), 
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)], 
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9), }[second] # 最后八位数字 
        suffix = random.randint(9999999,100000000) # 拼接手机号 
        return "1{}{}{}".format(second, third, suffix)

if __name__ == "__main__":
    r=Random()
    print r.RandomEmail()
    print r.Randomphone()
