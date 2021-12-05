from tkinter import *
import pymysql
connection=pymysql.connect(host='127.0.0.1',user='root',password='',db='phdbtech')

mycusrsor=connection.cursor()
root=Tk()
def msg():
    name=y.get()
    age= z.get()
    insert = "insert into test(name,age) values(%s,%s)"
    value = (name, age)
    mycusrsor.execute(insert, value)
    connection.commit()  # when we insert,update,delete to save data permananenly
    print("Data inserted successfully")



root.title("My Calculator")
lbl=Label(root,text="Enter Your name",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl.place(x=50,y=100)
#y=StringVar()
y=StringVar()
text=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=y)
text.place(x=300,y=100)


lbl1=Label(root,text="Enter Your Age",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"))
lbl1.place(x=50,y=150)
#y=StringVar()
z=IntVar()
text1=Entry(root,font=("Comic Sans MS",15,"bold"),bd="10",
           justify="right",textvariable=z)
text1.place(x=300,y=150)

btn=Button(root,text="SAve Data",bg="yellow",fg="red",
           font=("Comic Sans MS",15,"bold"),command=msg)
btn.place(x=100,y=250)





root.resizable(0,0)
root.geometry("800x400+320+200")
root.mainloop()