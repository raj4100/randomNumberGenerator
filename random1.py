import time
import math

def seed():
    return int(time.time())

def random_number(start=0,last=1,count=1):
    s = seed()   
    m = 1
    c = 11
    values = []
    c1 = int(0.27*count)
    var = 0
    lower = 0
    upper = 0
    mid = math.ceil((last-start+1)/2)
    for i in range(1,31):
        m = m*2
    m=m-1
    a=16807
    while ((lower < c1) or (upper < count-c1)):
        s=(a*s+c)%m
        temp=s%last
        if temp < start:
            temp=temp+start
        
        if ((temp <= mid) and (lower < c1)):
            lower=lower+1
            var=var+1
            values.insert(var,temp)
        elif ((temp > mid) and (upper < count-c1)):
            upper=upper+1
            var=var+1
            values.insert(var,temp)
        else:
            continue
    return ra
