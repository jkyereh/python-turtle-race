from turtle import Turtle
from random import randint

laura = Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160, 100)
laura.pendown()

larry = Turtle()
larry.color('blue')
larry.shape('turtle')
larry.penup()
larry.goto(-160, 70)
larry.pendown()

lau = Turtle()
lau.color('green')
lau.shape('turtle')
lau.penup()
lau.goto(-160, 40)
lau.pendown()

kofi = Turtle()
kofi.color('black')
kofi.shape('turtle')
kofi.penup()
kofi.goto(-160, 10)
kofi.pendown()

for movement in range(100):
    laura.forward(randint(1,5))
    larry.forward(randint(1,5))
    lau.forward(randint(1,5))
    kofi.forward(randint(1,5))
    
input("Press Enter to close")

