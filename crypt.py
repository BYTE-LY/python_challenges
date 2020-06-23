#!/bin/python3

# made by BYTE-LY

def crypt(self,key=5):
    return ''.join(chr(ord(i)*key) for i in self)

def decrypt(self,key=50):
    return ''.join(chr(int(ord(i)/key)) for i in self)
