# coding=utf-8

def bitset(x,n,V = 1):
    "sets bit n in array x to value V (0 or 1)"
    y = x
    y[n] = V
    return y

def bitshift(x,s):
    """shift x (number) by s bits.
    s > 0 -> left shift
    s < 0 -> right shift"""
    if s >= 0:
        return x << s
    else:
        return x >> s

def XOR(a, b):
    """XOR bitwise operator for input strings"""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

def AND(a,b):
    """AND bitwise operator for input strings/lists"""
    result = []
    for i in range(1, len(b)):
        if (a[i] == '1' and b[i] =='1') or (a[i] == 1 and b[i] == 1):
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)

def OR(a,b):
    """OR bitwise operator for input strings/lists"""
    result = []
    for i in range(1, len(b)):
        if (a[i] == '1' or b[i] =='1') or (a[i] == 1 or b[i] == 1):
            result.append('1')
        else:
            result.append('0')

    return ''.join(result)

def to_bit_array(x):
    res = []
    for i in x:
        res.append(int(i))
    return res

def to_bit_string(x)
    res=''
    for i in x:
        res.append(str(i))
    return res