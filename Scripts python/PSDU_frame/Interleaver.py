import numpy as numpy
import importlib
import random
import PHY_frame

sf1 = 31
sf2 = 64
lf1 = 11
lf2 = 21
sNi = 1024
lNi = 15120

def short_interleaver(index):
    s_int = sf1*index + (sf2*index^2 % sNi)
    return s_int

def long_interleaver(index):
    l_int = lf1*index + (lf2*index ^2 % lNi)
    return l_int

def interleave(data,typ):
    res = []
    z=[]
    if (typ is 'short' or typ is 's'):
        print 'Using short interleaver'
        for k in range(0,len(x)):
            z.append(short_interleaver(k%sNi))
        lim=max(z)
        res = [-1 for j in range(0,lim+1)]
        for i in range(0,len(x)):
            res[short_interleaver(i%sNi)] = data[i]
    elif (typ is 'long' or typ is 'l'):
        print 'Using long interleaver'
        for k in range(0,len(x)):
            z.append(long_interleaver(k%lNi))
        lim=max(z)
        res = [-1 for k in range(0,lim+1)]
        for i in range(0,len(x)):
            res[long_interleaver(i%lNi)] = data[i]
    else:
        raise Exception('Invalid input arguments')
    return res


x = [i for i in range(0,500)]
#z = []
z=interleave(x,'s')
print z
#y = interleave(x,'l')
#print y
# for k in range(0,len(x)):
#     z.append(long_interleaver(k%lNi))
# print max(z)
