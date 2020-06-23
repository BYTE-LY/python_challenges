#!/bin/python3

# make by BYTE-LY

def mask(self,visible=4):
    vis=self[-visible:]
    invis="*"*(len(self)-visible)
    return ('{}{}'.format(invis,vis))
