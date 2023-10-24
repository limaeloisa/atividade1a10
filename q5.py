import random
import turtle
jj = turtle.Turtle()
colors = ['black', 'blue' , 'gray' , 'pink']
jj.pensize(3)
jj.goto(50,0)
for _ in [1, 2, 3]:
    color = random.choice(colors)
    jj.color(color)
    jj.forward(120)
    jj.right(120)
jj.home()
for _ in [1, 2, 3, 4]:
  color = random.choice(colors)
  jj.color(color)
  jj.forward(220)
  jj.right(90)