from turtle import *
t=Turtle()  # crating turtle class object
t.speed(1)
t.color('red','green')
#t.pencolor('red')
t.pensize(5)

t.begin_fill()
t.forward(100)
t.left(90)
t.fd(100)  #forward=fd

t.left(90)
t.fd(100)

t.pencolor('green')
t.left(90)
t.fd(100)
t.end_fill()

done()
