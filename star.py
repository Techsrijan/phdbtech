from turtle import *
t=Turtle()
t.speed(10)
t.write("Mera Bharat Mahan")
l=['red','green','blue','yellow','orange']
for j in range(300):
    for i in range(5):
        t.pencolor(l[i])
        t.pensize(i/5+1)
        t.forward(300)
        t.left(216-j)
done()