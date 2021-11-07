from turtle import *
t=Turtle()
t.circle(50)
t.circle(-50)
#t.reset()
t.undo()
t.penup()
#t.forward(100)
t.goto(100,50)
t.pendown()
t.circle(100,steps=5)

done()