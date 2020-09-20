import numpy as np
from numpy import binary_repr as br


#con deconvolucion/division polinomial
def crc4_num(msg):
    """CRC-4 implementation numerical"""
    N = len(msg)
    poly = [1, 0, 0, 1, 1]  # x^4 + x + 1
    msg.append([0, 0, 0, 0, 0])
    ra = []
    q, r = np.polydiv(msg, poly)
    for i in range(0, np.size(r)):
        ra.append(abs(r[i]) % 2)

    crc = ra[N + 1:]
    return crc


def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


# Performs Mod-2 division for crc
#with xor
def mod2div(msg, poly):
    pick = len(poly)
    tmp = msg[0: pick]

    while pick < len(msg):
        if tmp[0] == '1':
            tmp = xor(poly, tmp) + msg[pick]

        else:
            tmp = xor('0' * pick, tmp) + msg[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(poly, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    crc = tmp
    return crc


def header(dataRate, length, burst, seed1, seed2, ft):
    # PHY layer frame header structure

    if ((dataRate > 7 or dataRate <= 0) or (length > 127 or length < 0) or (seed1 >= 2 ** 6 or seed1 < 0) or (
            seed2 >= 2 ** 6 or seed2 < 0)
            or (burst != 0 and burst != 1) or (ft != 0 and ft != 1)):
        raise Exception('Invalid input arguments')

    header = []
    for i in range(0, 32):
        header.append(0)

    bindr = br(dataRate, 3)
    bindr_le = [int(bindr[-1]), int(bindr[-2]), int(bindr[-3])]
    header[0:3] = bindr_le[:]
    header[3] = int(br(0, 1))  # "reserved"

    binl = br(length, 8)
    binl_le = [int(binl[-1]), int(binl[-2]), int(binl[-3]), int(binl[-4]), int(binl[-5]), int(binl[-6]),
               int(binl[-7]), int(binl[-8])]
    header[4:12] = binl_le[:]
    header[12:14] = [int(br(0, 1)), int(br(0, 1))]  # "reserved"

    header[14] = burst  # 1 o 0 para ver si esta activado

    bins1 = br(seed1, 6)
    bins1_le = [int(bins1[-1]), int(bins1[-2]), int(bins1[-3]), int(bins1[-4]), int(bins1[-5]), int(bins1[-6])]
    header[15:21] = bins1_le[:]

    bins2 = br(seed2, 6)
    bins2_le = [int(bins2[-1]), int(bins2[-2]), int(bins2[-3]), int(bins2[-4]), int(bins2[-5]), int(bins2[-6])]
    header[21:27] = bins2_le[:]

    header[27] = int(br(ft, 1))  # (0 for type I, 1 for type II)
    head =[]

    for i in range(0, len(header)):
        head.append(str(header[i]))

    crc = mod2div(head, '10011')
    #print 'crc-4: ' + str(crc)
    header[28:32] = [int(crc[0]), int(crc[1]), int(crc[2]), int(crc[3])]
    return header


def create_frame(header, input):
    f = []
    for i in range(0, len(header)):
        f.append(br(header[i], 1))

    for j in range(0, len(input)):
        f.append(br(input[j], 1))
    return f


""" msg_in = [1,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1]
M = len(msg_in)
head = header(1, M, 0, 12, 6, 0)
poly = '10011' #crc-4
N = len(poly)-1  #long crc
frm = create_frame(head, msg_in)
crc = mod2div(frm, poly)
print type(crc)
for k in range(0, len(crc)):
    frm.append(br(int(crc[k]), 1))

x = M + len(head) + len(crc)
print x
print 'Frame: '
print frm
print len(frm) """
