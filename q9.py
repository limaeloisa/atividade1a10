import turtle
import random
e = turtle.Turtle()
e.shape('turtle')
colors = ['violet', 'blue', 'green', 'red', 'gray', 'purple', 'pink', 'indigo']
for c in range(360):
    color = random.choice(colors)
    e.forward(2)
    e.color(color)
    e.left(1)