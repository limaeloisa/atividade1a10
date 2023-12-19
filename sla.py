from turtle import Turtle, Screen

tela = Screen

e = Turtle()

def circle():
    e.circle(34)

def squad():
    for i in range():
        e. forward(100)
        e. left(90)

def pencolor():
    e.pencolor('')

escolha = " "
cor = "  "

while(escolha !=0):
    print("---------------------------")
    print("1: Circle")
    print("2: Squad")
    escolha = int(input("qual vc quer?"))
    if escolha == 1:
        circle()
    if escolha == 2:
        squad()


while (cor !=0):
    print ("pencolor:")
    color = int(input("qual cor vc quer?"))
    if cor:
        e.pencolor()


tela.mainloop()