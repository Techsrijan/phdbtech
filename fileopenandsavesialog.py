from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog

def color_choose():
    c=colorchooser.askcolor()
    txt.configure(background=c[1])
    print(c)

def color_choose2():
    c=colorchooser.askcolor()
    txt.configure(foreground=c[1])
    print(c)

def open_file():
    f=filedialog.askopenfile(mode="r",initialdir="/",
                             title="Select file",
                             filetypes=(("Text file", "*.txt"), ("All files", "*.*"))
                             )
    print(f)
    for data in f:
        print(data)
        txt.insert(INSERT, data)
root=Tk()
txt=Text(root,width=20,height=5,wrap=WORD,selectbackground='red')
txt.insert(INSERT,"Welcome to this note pad")
txt.pack()

btn1=Button(root,text="Change background color",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=color_choose)
btn1.pack()

btn2=Button(root,text="Change foreground color",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=color_choose2)
btn2.pack()

btn3=Button(root,text="open file",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=open_file)
btn3.pack()

root.geometry("800x600+320+200")
root.mainloop()
