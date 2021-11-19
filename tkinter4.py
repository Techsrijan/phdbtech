from tkinter import *
root=Tk()
def msg():
    a=y.get()
    print(a)
    b= z.get()
    c=a+b
    r.set(c)
    print(a+b)


root.title("My Calculator")
lbl=Label(root,text="Enter first Number",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl.place(x=50,y=100)
#y=StringVar()
y=IntVar()
text=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=y)
text.place(x=300,y=100)


lbl1=Label(root,text="Enter Second Number",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl1.place(x=50,y=150)
#y=StringVar()
z=IntVar()
text1=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=z,show="*")
text1.place(x=300,y=150)

btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg)
btn.place(x=100,y=250)

lbl3=Label(root,text="Your Result is",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl3.place(x=50,y=300)
#y=StringVar()
r=IntVar()
text3=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=r)
text3.place(x=300,y=300)



root.resizable(0,0)
root.geometry("800x400+320+200")
root.mainloop()