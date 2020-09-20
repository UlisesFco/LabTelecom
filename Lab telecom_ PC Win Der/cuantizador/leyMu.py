#!usr/bin/env python2

import numpy as np
from matplotlib import pyplot as plt

#ley mu
factor = 0

def uniform_quantizer(X, B):
    x = X
    #Paso del cuantizador
    Q = np.float(np.max(x) - np.min(x))/np.float(2**B)
    Qa = []
    #Calculo del indice de la cuantizacion
    for k in range(0,np.size(x)):
    	s = float(x[k]/Q)
    	Qa.append(s + 0.5)

    xQ = (Q * (np.floor(Qa)))
    return xQ

def mu_compressor(x,mu=255):
	"""u-law compressor, default for u=255 and input x"""
	z=[]
	M = np.max(x)
	m = np.absolute(np.min(x))
	global factor
	factor = np.max([M,m])
	#normalizando la entrada
	for k in range(0,np.size(x)):
		aux = np.float(x[k]/factor)
		z.append(aux)

	Fz = []
	#realizando la compresion
	for k in range(0,np.size(z)):
		aux = np.sign(z[k])*(np.log(1+mu*np.absolute(z[k])))/np.log(1+mu)
		Fz.append(aux)

	return Fz

def mu_expander(z,mu=255):
	"""u-law expander, default for u=255 
	(same value as the one for compression) and input z"""
	w=[]
	M = np.max(z)
	m = np.absolute(np.min(z))
	f = np.max([M,m])
	#normalizando la entrada
	for k in range(0,np.size(z)):
		aux = np.float(z[k]/f)
		w.append(aux)

	Gw = []
	#realizando la compresion
	print factor
	for k in range(0,np.size(w)):
		aux = np.sign(w[k])*(np.power(1+mu,np.absolute(w[k]))-1)/mu
		Gw.append(aux)
		Gw[k] = Gw[k]*factor
	return Gw

def plot_signals(x,xC,xQ,xD):
	#x -> senal original
	#xQ -> senal cuantizada
	#N -> num de muestras
    e = xQ - xC
    plt.figure(figsize=(10,6))
    plt.title('Ley mu')
    plt.plot(x, label=r'original signal $x[k]$',color='black')
    plt.plot(e, label=r'quantization error (compressed signal) $E_Q[k]$',color='red')
    plt.plot(xC, label=r'compressed signal $x_C[k]$',color='blue')
    plt.plot(xQ, label=r'quantized signal $x_Q[k]$',color='green')
    plt.plot(xD, label=r'decompressed signal $x_D[k]$',color='orange')
    plt.xlabel(r'$k$')
    #plt.axis([0, np.size(x), -1.1*min(x), 1.1*max(x)])
    plt.legend(loc='upper right')
    plt.grid()
    plt.show()


n = 2000
A = 1.2
b = input('Numero de bits: ')
mu = input('Valor de mu: ')
t = np.linspace(0,2*np.pi,1000)
x = np.sin(2*np.pi*t) + np.cos(np.pi*t) + np.random.normal(0,1,np.size(t))
# quantize signal
xC = mu_compressor(x,mu)
xQ = uniform_quantizer(xC, b)
xD = mu_expander(xQ,mu)
sqnr = 6*b - 7.2;
print("SQNR= %d" %sqnr)
plot_signals(x,xC,xQ,xD)