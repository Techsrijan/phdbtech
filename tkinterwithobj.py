from tkinter import *

class MyWindow:
    def __init__(self,window):
        self.btn=Button(window,text="clickme")
        self.btn.pack()


root=Tk()
wn=MyWindow(root)

root.geometry("400x400+320+200")
root.mainloop()