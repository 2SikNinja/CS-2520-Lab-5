#Authors: Peter Nguyen
#Assignment: Lab #5
#Completed (or last revision): 10/06/2022
from turtle import *
from random import *
x = 1
bgcolor('black')
speed(0)
while x < 600:
    r = randint(0,255) 
    g = randint(0,255)  
    b = randint(0,255) 
    colormode(255)
    pencolor(r,g,b)
    fd(100 + x)
    rt(90.991)
    x+=2
done()