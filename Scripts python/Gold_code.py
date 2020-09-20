# coding=utf-8
import sympy as sp
import numpy as np
from fractions import gcd
import bitwise_operators_strings as bw

def shift_register(iniCond,poly):
    """Generates a maximum length sequence in a shift register from the next arguments: 
    - iniCond: the initial condition of the shift register
    - poly: primitive polynomial in binary format
    both arguments are strings in binary format, i.e '1011'."""
    
    if len(iniCond) != len(poly):
        raise Exception('Argument length mismatch')
    
    regSize = len(poly)
    Rg = int(iniCond,2)
    g = int(poly,2)
    N = 2**regSize - 1
    
    for i in range(0,N+1):
        if Rg & 1 != 0

    

def gold_sequence(iniCond,poly):
    """Generates a Gold code sequence from the next parameters:
    - iniCond: the initial condition of the shift register
    - poly: primitive polynomial in binary format
    both arguments are strings in binary format, i.e '1011'."""
    
    if len(iniCond) != len(poly):
        raise Exception('Argument length mismatch')
    regSize = len(poly)
    N = 2**regSize -1
    if regSize%4 != 0:
        if regSize%4 == 2:
            e,k = 2,1
            while gcd(regSize,k) != 2:
                k+=1
            f = 2**k+1
        else:
            e,k = 1,1
            while gcd(regSize,k) != 1
                k+=1
            f= 2**k + 1
    else:
        raise Exception('No available sequences for the given arguments')
    
    SR1 = shift_register(iniCond,poly)
    SR2 = []
    for i in range(0,N):
        k = (i*f % N) + 1
        SR2.append(SR1[k])
    
    G = -2*xor(SR1,SR2) + 1 
    print(G)
    Gs = bw.toArray(G)
    np.corrcoef(Gs,Gs)
    return Gs

gold_sequence('0001','1011')