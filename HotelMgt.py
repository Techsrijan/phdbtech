from tkinter import *
import pymysql
taz=Tk()
width=taz.winfo_screenwidth()
#print(width)
height=taz.winfo_screenheight()
#print(height)
#### database Connection ################
def dbconfig():
    global mycursor, conn
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='phdbtech')
    mycursor = conn.cursor()

#### mainheading ##############################
def mainheading():
    label = Label(taz, text="Hotel WahTaz Management system", bg="yellow", fg="green",
                  font=("Comic Sans Ms", 38, "bold"), padx=40, pady=0)
    label.grid(row=0, columnspan=4)

mainheading()
taz.title("Hotel Managment System")
taz.geometry("%dx%d+0+0"%(width,height))
taz.mainloop()