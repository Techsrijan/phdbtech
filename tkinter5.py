from tkinter import *
root=Tk()
def msg(event):
    print("Good Morning")

def msg2(event):
    print("Good Afternoon")

def msg3(event):
    print("Good Evening")




root.title("My Calculator")
root.bind("<Control-t>",msg)
btn=Button(root,text="Button1",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
btn.pack(side=TOP)
btn.bind("<Button-1>",msg)
btn1=Button(root,text="Button2",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
btn1.pack(side=BOTTOM)
btn1.bind("<Button-2>",msg2)
btn2=Button(root,text="Button3",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
btn2.pack(side=LEFT,fill=Y)
btn2.bind("<Button-3>",msg3)
#root.resizable(0,0)
root.geometry("400x400+320+200")
root.mainloop()