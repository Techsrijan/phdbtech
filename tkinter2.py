from tkinter import *
root=Tk()
def msg():
    print("Good Morning")

def msg2():
    print("Good Afternoon")
root.title("My Calculator")
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg)
btn.pack(side=TOP)

btn1=Button(root,text="Press Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg2)
btn1.pack(side=BOTTOM)

btn2=Button(root,text="Press Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg2)
btn2.pack(side=LEFT,fill=Y)
#root.resizable(0,0)
root.geometry("400x400+320+200")
root.mainloop()