#!usr/bin/env python2

import numpy as np
from matplotlib import pyplot as plt
# Paso = (max-min)/(N) -> N=2^B
#A = 1.2  # amplitude of signal
  # quantization stepsize
#n = 2000  # number of samples
#x -> entrada
#Q ->paso del cuantizador
#N -> numero de niveles
#B -> numero de bits
#xq = floor(x*(2^B-1)/(max{x}-min{x}))

def uniform_quantizer(X, B):
    # limiter
    #paso del cuantizador
    x = X
    Q = np.float(np.max(x) - np.min(x))/np.float(2**B)
    #idx = np.where(np.abs(x) >= 1)
    #x[idx] = np.sign(x[idx])
    # linear uniform quantization
    Qa = []
    for k in range(0,np.size(x)):
    	s = float(x[k]/Q)
    	Qa.append(s + 0.5)

    xQ = (Q * (np.floor(Qa)))#*((2**B -1)/2) #para normalizar a numero de bits
    print("se usaron %d bits" %B)
    return xQ

# def bit_stream(xQ,B):
# 	#xQ-> senal cuantizada
# 	#B-> num de bits
# 	Q = np.float(np.max(xQ) - np.min(xQ))/np.float(2**B)
# 	for i in range(-2**(B-1),2**(B-1)):


# 	xQ = xQ*((2**B -1)/2) 
# 	bits = []
# 	for i in range(0,np.size(xQ)):
# 		if (xQ[i]>0):
			
# 		else:

# 	return bits

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
    #plt.axis([0, np.size(x), -1.1*min(x), 1.1*max(x)])
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()

#if __name__ == "__main__":
# generate signal
	#import numpy as np
	#import matplotlib.pyplot as plt

n = 2000
A = 1.2
b = 4
t = np.linspace(0,6,200)
x = np.sin(2*np.pi*t) #+ np.random.normal(0,0.5,np.size(t))
# quantize signal
xQ = uniform_quantizer(x, b)
#print(xQ)
# plot signals
plot_signals(x, xQ,b)