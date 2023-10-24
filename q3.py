import turtle

jose = turtle.Turtle()
jose.shape('triangle')
jose.pensize(4)

for color in ['green', 'purple', 'blue', 'red']:
    jose.color(color)
    jose.forward(150)
    jose.right(90)