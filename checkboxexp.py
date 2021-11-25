from tkinter import *
root=Tk()
def getdata():
    print(i.get())
    print(j.get())
f=LabelFrame(root,text="Select Language Known")
i=IntVar()
j=IntVar()
r1=Checkbutton(f,text="Hindi",variable=i)
r2=Checkbutton(f,text="English",variable=j)
r1.pack()
r2.pack()
f.pack()

btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=getdata)
btn.pack()
root.geometry("400x400+320+200")
root.mainloop()