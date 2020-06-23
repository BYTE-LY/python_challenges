#!/bin/python3

# make by BYTE-LY

def random_user():
    return("USER: {}".format(''.join(list(set(['A','B','C','D','E','G','J','K','P','Q','Z','X','U','K','I']))[i] for i in range(8))))

def random_pass():
    return("PASS: {}".format(''.join(list(set(['A','a','X','b','1','2','3','5','6','7','9','Z','f','R','r','K']))[i] for i in range(8))))

def random_ip():
   return("IP  : {}".format('.'.join(list(set([str(i) for i in range(1,255)]))[i] for i in range(4))))
