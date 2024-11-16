#! /usr/bin/env python3

def soln(a, b):
    a = binary2decimal(a)
    b = binary2decimal(b)
    s = a+b
    return decimal2binary(s)

def binary2decimal(bi):
    # 1101 -> 2**3 * 1 + 2**2 * 1 + 2**1 * 0 + 2**0 * 1
    exp = len(bi)-1
    dec = 0
    for c in bi:
        dec += 2**exp * int(c)
        exp -= 1
    return dec

def decimal2binary(dec):
    if dec==0: return "0"
    tmp = int(dec)
    bin = ""
    while tmp>=1:
        bin+=str(tmp%2)
        tmp = tmp//2
    ret = list(bin)
    ret.reverse()
    bin = ""
    for e in ret:
        bin+=e
    return bin

#print(binary2decimal("0"))
print(decimal2binary(0))
