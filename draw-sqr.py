#!/bin/python

#Draw a sqare with a pre defind char and lenght
#length support range(0,infinity)
#by BYTE-LY

def sqr(l,symbol):
    return "\n".join([symbol*l,'\n'.join('{0}{1}{0}'.format(symbol,(' '*len(symbol)*l)[:-2*len(symbol)])for i in range(l-2)),(symbol*l if l > 1 else ' ')])
