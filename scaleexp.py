from tkinter import *
root=Tk()
def msg():
    print(s.get())
    print(spin.get())

spin=Spinbox(root,from_=1,to=5)
spin.pack()
s=Scale(root,from_=100,to=200,orient=HORIZONTAL,length=200,width=20,sliderlength=50)
s.set(155)
s.pack()
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg)
btn.pack(side=TOP)


#root.resizable(0,0)
root.geometry("400x400+320+200")
root.mainloop()