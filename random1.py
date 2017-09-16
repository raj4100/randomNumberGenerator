import time
import math

def seed():
    return int(time.time())

def random_number(start=0,last=1,count=1):
    s = seed()   
    m = 1
    c = 11
    ra = []
    c1 = int(0.27*count)
    c2 = count-c1
    var = 0
    x = 0
    r = 0
    mid = math.ceil((last-start+1)/2)
    for i in range(1,31):
        m = m*2
    m=m-1
    a=16807
    while ((x < c1) or (r < c2)):
        s=(a*s+c)%m
        l=s%last
        if l < start:
            l=l+start
        
        if ((l <= mid) and (x < c1)):
            x=x+1
            var=var+1
            ra.insert(var,l)
        elif ((l > mid) and (r < c2)):
            r=r+1
            var=var+1
            ra.insert(var,l)
        else:
            continue
    return ra
