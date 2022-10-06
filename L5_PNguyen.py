#Authors: Peter Nguyen
#Assignment: Lab #5
#Completed (or last revision): 10/06/2022
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
#EPILEPSY WARNING!!!!! THIS CREATES A STAR WITH FLASHING LIGHTS
from turtle import *
from random import *
import time
clock = time
x = 1
bgcolor('black') #start the background with the color black
speed(0)
while x < 600:
    r = randint(0,255) #create rgb values using random integers
    g = randint(0,255)  
    b = randint(0,255) 
    colormode(255) #set the color mode of the pen which is rgb values
    pencolor(r,g,b) #changes the pen color each iteration
    fd(100 + x) #forward by 101 at the start
    rt(150) #rotates the cursor by 150
    x+=2 #iterate the amount cursor goes forward in order to increase the size of the shape
    bgcolor(r,g,b) #changes the background color each time to make rainbows
while(True): #this is just to display the art when completed flashing in black and white
    bgcolor('black')
    time.sleep(.9)
    bgcolor('white')
    time.sleep(.9)