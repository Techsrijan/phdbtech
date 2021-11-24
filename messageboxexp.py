from tkinter import *
from tkinter import messagebox
root=Tk()
def fun():
    #res=messagebox.askyesno("Confirmation Box","Do u ant to save this file?")
    #res = messagebox.showwarning("Confirmation Box", "Do u ant to save this file?")
    res = messagebox.askyesnocancel("Confirmation Box", "Do u ant to save this file?")
    print(res)
    if res==True:
        print("file is saved")
btn1=Button(root,text="Press Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=fun)
btn1.place(x=200,y=150)

btn2=Button(root,text="Close",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=quit)
btn2.place(x=100,y=150)
root.geometry("400x400+320+200")
root.mainloop()