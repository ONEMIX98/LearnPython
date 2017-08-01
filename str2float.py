# -*- coding: utf-8 -*-

from functools import reduce

def str2float(s):
    d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    def str2int(s):
        return reduce(lambda x,y: 10*x + y, map(lambda char: d[char], s))
    idx = s.find('.')
    #没有小数点
    if idx == -1:
        return str2int(s)
    else:
        s = s.replace('.','')
        return str2int(s)/pow(10, len(s)-idx)




#test:
print('str2float(\'123.456\') =', str2float('123.456'))
