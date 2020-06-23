#!/bin/python3

# This script draws four contry flags that start with the letter 'B'
# this is made using the turtle graphics lib
# by BYTE-LY

import turtle
from time import sleep

def pixel(color,X,Y,bg='white'):
    x=turtle.Turtle()
    x.screen.bgcolor(bg)
    x.speed(200)
    x.color(color),x.up()
    x.forward(50*X)
    x.left(90),x.forward(50*Y),x.right(90)
    x.down(),x.begin_fill()
    for i in range(4):
         x.forward(50),x.right(90)
    x.end_fill()

def tria(color,x1,y1,x2,y2):
    x=turtle.Turtle()
    #x.speed(150)
    x.color(color)
    x.begin_fill()
    x.down()
    x.goto(x1,y1)
    x.goto(x2,y2)
    x.end_fill()

def belgium():
    for i in range(3):
        pixel('black',0,i)
        pixel('yellow',1,i)
        pixel('red',2,i)

def bulgaria():
    for i in range(3):
        pixel('red',i,0,'black')
        pixel('green',i,1,'black')
        pixel('white',i,2,'black')

def benin():
    for i in range(4):
        pixel('green',0,i)

    for i in range(1,4):
        for u in range(2):
            pixel('red',i,u)
            pixel('yellow',i,u+2)

def bahamas():
    for i in range(6):
        pixel('blue',i,0)
        pixel('blue',i,1)
        pixel('yellow',i,2)
        pixel('black',i,3)
        pixel('yellow',i,4)
        pixel('blue',i,5)
        pixel('blue',i,6)

    tria('black',150,150,0,300)

def main():
    belgium()
    sleep(3)
    bulgaria()
    sleep(3)
    benin()
    sleep(3)
    bahamas()
    sleep(3)

if __name__=='__main__':
    main()
