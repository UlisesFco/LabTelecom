#!usr/bin/env python2

import numpy as np
from matplotlib import pyplot as plt

#ley A
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

def A_compressor(x,A=255):
	"""A-law compressor, default for A=255 and input x"""
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
		if (np.absolute(z[k])<1/A):
			aux = np.sign(z[k])*(A*np.absolute(z[k]))/(1+np.log(A))
		else:
			aux = np.sign(z[k])*(1 + np.log(A*np.absolute(z[k])))/(1+np.log(A))
		Fz.append(aux)

	return Fz

def A_expander(z,A=255):
	"""A-law expander, default for A=255 
	(same value as the one for compression) and input z"""
	w=[]
	M = np.max(z)
	m = np.absolute(np.min(z))
	f = np.max([M,m])
	global factor
	#normalizando la entrada
	for k in range(0,np.size(z)):
		aux = np.float(z[k]/f)
		w.append(aux)

	Gw = []
	#realizando la compresion
	for k in range(0,np.size(w)):
		if (np.absolute(w[k])<1/(1+np.log(A))):
			aux = np.sign(w[k])*(np.absolute(w[k])*(1+np.log(A)))/A
		else:
			aux = np.sign(w[k])*(np.exp(np.absolute(w[k])*(1+np.log(A))-1))/A
		Gw.append(aux)
		Gw[k] = Gw[k]*factor
	return Gw

def plot_signals(x,xC,xQ,xD):
	#x -> senal original
	#xQ -> senal cuantizada
	#N -> num de muestras
    e = xQ - xC
    plt.figure(figsize=(10,6))
    plt.title('Ley A')
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
b = input('Numero de bits: ')
A = input('Valor de A: ')
t = np.linspace(0,2*np.pi,1000)
x = np.sin(2*np.pi*t) + np.cos(np.pi*t) #+ np.random.normal(0,0.5,np.size(t))
# quantize signal
xC = A_compressor(x,A)
xQ = uniform_quantizer(xC, b)
xD = A_expander(xQ,A)
sqnr = 6*b - 7.2;
print("SQNR= %d" %sqnr)
plot_signals(x,xC,xQ,xD)