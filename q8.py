import turtle
import random

import turtle
import random

i = turtle.Turtle()
colors = ['purple', 'blue', 'brown' , 'gray' , 'black', 'violet', 'red' , 'orange']
i.pensize (3)

for _ in range (9):
    color = random.choice(colors)
    i.color(color)
    i.forward(100)
    i.backward(100)
    i.right(45)
for _ in range (8):
    i.right(69)
    i.forward(100)
    i.backward(100)
    i.right(65)