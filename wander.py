from turtle import*
from random import randint
speed(1000)
def wander():
    while True:
        fd(1)
        if xcor()>=200 or xcor()<=-200 or ycor()>=200 or ycor()<=-200:
            lt(randint(90, 180))
wander()
#this is the pgm
