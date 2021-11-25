from tkinter import *
from tkinter import ttk

def getdata():
    val=c.get()
    print(val)
root=Tk()
course=['c','java','python','php']
c=ttk.Combobox(root,value=course)
c.set("Select Course ")
c.pack()
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=getdata)
btn.pack()
root.geometry("400x400+320+200")
root.mainloop()