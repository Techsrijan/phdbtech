from tkinter import *
from tkinter import simpledialog
root=Tk()
def msg():
    sum=0
    for i in range(5):
        s=simpledialog.askinteger("Marks Input Box","Enter the marks of student")
        sum=sum+s
    print(sum)

btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg)
btn.pack(side=TOP)


#root.resizable(0,0)
root.geometry("400x400+320+200")
root.mainloop()