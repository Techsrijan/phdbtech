from turtle import *


def sq():
    t.forward(100)
    t.left(90)

t=Turtle()
sc=Screen()
sc.setup(600,400)
#sc.bgcolor('#76c4f9')
sc.bgpic('test.gif')
sc.title("Mera Turtle")


t.shape('turtle')
t.hideturtle()
for i in range(4):
    sq()

t.right(90)
t.penup()   #pu
t.forward(100)
t.pendown()   #pd

for i in range(4):
    sq()

done()