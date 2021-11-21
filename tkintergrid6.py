from tkinter import *
root=Tk()

text33=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",show="*")
text33.grid(row=0,columnspan=2)
lbl1=Label(root,text="Enter ",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl1.grid(row=1,column=0)

z=IntVar()
text1=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=z,show="*")
text1.grid(row=1,column=1)
lbl2=Label(root,text="Enter",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl2.grid(row=2,column=0)

z=IntVar()
text2=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=z,show="*")
text2.grid(row=2,column=1)
root.wm_iconbitmap('notepad.ico')
root.mainloop()