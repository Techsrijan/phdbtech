from tkinter import *
root=Tk()
def getdata():
    print(i.get())

f=LabelFrame(root,text="Select Gender")
i=IntVar()
r1=Radiobutton(f,text="Male",value=1,variable=i)
r2=Radiobutton(f,text="FeMale",value=2,variable=i)
r1.pack()
r2.pack()
f.pack()

f1=LabelFrame(root,text="Select Gender")
i=IntVar()
r11=Radiobutton(f1,text="Male",value=1,variable=i)
r22=Radiobutton(f1,text="FeMale",value=2,variable=i)
r11.pack()
r22.pack()
f1.pack()
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=getdata)
btn.pack()
root.geometry("400x400+320+200")
root.mainloop()