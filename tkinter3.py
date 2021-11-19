from tkinter import *
root=Tk()
def msg():
    print("Good Morning")

def msg2():
    print("Good Afternoon")
root.title("My Calculator")
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg)
btn.place(x=50,y=150)

btn1=Button(root,text="Press Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=msg2)
btn1.place(x=200,y=150)


#root.resizable(0,0)
root.geometry("400x400+320+200")
root.mainloop()