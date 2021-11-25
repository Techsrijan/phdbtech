from tkinter import *
root=Tk()
def getdata():
    data=l.curselection()
    print(data)
    for i in data:
        print(l.get(i))

def deldata():
    data = l.curselection()
    print(data)
    for i in data:
        print(l.delete(i))


root.title("My Calculator")

l=Listbox(root,height=5,selectmode=EXTENDED)
l.insert(0,"Papad")
l.insert(1,"Paneer")
l.insert(2,"Tea")
l.insert(3,"Chawal")
l.insert(4,"Paneer")
l.insert(5,"Tea")
l.insert(6,"Chawal")


l.pack()
btn=Button(root,text="Click Me",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=getdata)
btn.pack()

btn2=Button(root,text="delete item",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=deldata)
btn2.pack()
#root.resizable(0,0)
root.geometry("400x400+320+200")
root.mainloop()