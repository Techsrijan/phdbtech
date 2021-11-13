from turtle import *
t=Turtle()
t.write("Mera Bharat Mahan",font=("Arial", 24, "normal"))
sc=Screen()
def move_x():
    t.forward(100)

def move_y():
    t.backward(200)

def change_dir():
    t.left(90)
sc.listen()
sc.onkey(move_x,'Up')
sc.onkey(move_y,'Down')
sc.onkey(change_dir,'d')
done()