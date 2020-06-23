#!/bin/python3

# made by BYTE-LY

def letter_order2(self):
    return' '.join("\' \'" if (ord(str.upper(i))-64)==-32 else str(ord(str.upper(i))-64) for i in self)
