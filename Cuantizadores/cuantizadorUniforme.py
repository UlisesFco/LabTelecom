#!usr/bin/env python2

import numpy as np
from matplotlib import pyplot as plt

def uniform_quantizer(X, B):
    # limiter
    #paso del cuantizador
    x = X
    Q = np.float(np.max(x) - np.min(x))/np.float(2**B)
    # linear uniform quantization
    Qa = []
    for k in range(0,np.size(x)):
    	s = float(x[k]/Q)
    	Qa.append(s + 0.5)

    xQ = (Q * (np.floor(Qa)))#*((2**B -1)/2) #para normalizar a numero de bits
    print("se usaron %d bits" %B)
    return xQ

def plot_signals(x, xQ,B):
	#x -> senal original
	#xQ -> senal cuantizada
	#N -> num de muestras
    e = xQ - x
    plt.figure(figsize=(10,6))
    plt.plot(x, label=r'original signal $x[k]$',color='blue')
    plt.plot(e, label=r'quantization error $E_Q[k]$',color='orange')
    plt.plot(xQ, label=r'quantized signal $x_Q[k]$',color='red')
    plt.xlabel(r'$k$')
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

n = 2000
A = 1.2
b = 4
t = np.linspace(0,6,200)
x = np.sin(2*np.pi*t)
# quantize signal
xQ = uniform_quantizer(x, b)
#print(xQ)
# plot signals
plot_signals(x, xQ,b)
