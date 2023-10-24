import turtle
import random
ze = turtle.Turtle()
colors = ['black', 'purple', 'blue' , 'gray' , 'pink']
ze.pensize(3)
for _ in [1, 2, 3]:
    color = random.choice(colors)
    ze.color(color)
    ze.forward(100)
    ze.left(120)