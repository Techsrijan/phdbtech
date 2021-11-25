from tkinter import *
root=Tk()
f=Frame(root)
scroll=Scrollbar(f)
scroll.pack(side=RIGHT,fill=Y)
l=Listbox(f,height=5,selectmode=EXTENDED)
for i in range(1,32):
    l.insert(END,"Mylist"+str(i))

scroll.config(command=l.yview)
l.pack()
f.pack()
root.geometry("400x400+320+200")
root.mainloop()