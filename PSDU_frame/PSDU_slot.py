# coding=utf-8
import numpy as np
import random

def OFDM_sym(data):
    i=1024
    j=0
    first = True
    sym = []
    if len(data) > 1024:
        while(j*i < len(data)):
            y = data[j:i]
            aux = np.fft.fft(y,1024)
            if first:
                guard = aux[1024-74:]
            else:
                guard = aux[1024-73:]
            i,j = i+i,i
            sym.append(guard)
            sym.append(aux)
            first = False
    y = data[j:]
    aux = np.fft.fft(y,1024)
    if first:
        guard = aux[1024-74:]
    else:
        guard = aux[1024-73:]
    sym.append(guard)
    sym.append(aux)
    return sym

x = [random.randint(-128,128) for _ in range(1025)]
res = OFDM_sym(x)
print res





