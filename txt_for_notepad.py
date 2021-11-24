from tkinter import *
def get_data():
    res=txt.get(1.0,END)
    print(res)

def get_selected_data():
    result=txt.selection_get()
    print(result)
    print(len(result))
    pos=txt.search(result,1.0,stopindex=END)
    print(pos)
    for i in range(len(result)+1):
        txt.delete(pos,None)


def clear_data():
    txt.delete(1.0,END)
root=Tk()
txt=Text(root,width=20,height=5,wrap=WORD,selectbackground='red')
txt.insert(INSERT,"Welcome to this note pad")
txt.pack()

btn1=Button(root,text="GET Text BOX DATA",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=get_data)
btn1.pack()

btn2=Button(root,text="GET Selected Text BOX DATA",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=get_selected_data)
btn2.pack()


btn3=Button(root,text="Clear Text BOX DATA",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),bd=10,command=clear_data)
btn3.pack()
root.geometry("800x600+320+200")
root.mainloop()
