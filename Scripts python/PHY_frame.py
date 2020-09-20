import numpy as np
from numpy import binary_repr as br
from matplotlib import pyplot as plt
from scipy import signal

msg_in = [1,0,1,0,1,0,1,0,1,0];
M = len(msg_in)


def crc4_num(msg):
	"""CRC-4 implementation"""
	N = len(msg)
	poly = [1,0,0,1,1] #x^4 + x + 1
	msg.append([0,0,0,0,0])
	ra = []
	q,r = np.polydiv(msg,poly)
	for i in range(0,np.size(r)):
		ra.append(abs(r[i])%2)

	crc = ra[N+1:]
	return crc



def header(dataRate,length,burst,seed1,seed2,ft):
	#PHY layer frame header structure
   
    if ((dataRate>7 or dataRate <=0) or (length >127 or length <0) or (seed1>=2**6 or seed1<0) or (seed2>=2**6 or seed2<0)
    	or (burst!=0 and burst != 1) or ( ft!=0 and ft != 1)):
    	raise Exception('Invalid input arguments')
    	
    header=[]
    for i in range(0,32):
        header.append(0)


    bindr = br(dataRate,3)
    bindr_le = [bindr[-1], bindr[-2], bindr[-3]]
    header[0:3]=bindr_le[:]
    header[3] = 0; #"reserved"

    binl = br(length,8);
    binl_le = [binl[-1], binl[-2], binl[-3], binl[-4], binl[-5], binl[-6], binl[-7], binl[-8]]
    header[4:12] = binl_le[:];
    header[12:14] = [0,0] #"reserved"

    header[14] = burst #1 o 0 para ver si esta activado

    bins1 = br(seed1,6);
    bins1_le = [bins1[-1], bins1[-2], bins1[-3], bins1[-4], bins1[-5], bins1[-6]]
    header[15:21] = bins1_le[:]

    bins2 = br(seed2,6);
    bins2_le = [bins2[-1], bins2[-2], bins2[-3], bins2[-4], bins2[-5], bins2[-6]]
    header[21:27] = bins2_le[:]

    header[27] = str(ft) + ''; #(0 for type I, 1 for type II)
    #crc = crc4_num(msg_in)
    #print len(crc)
    #header[28:32] = crc[:]
    print header
    return header


test=header(5,M,0,15,2,0)