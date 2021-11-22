from tkinter import *

root=Tk()
canvas=Canvas(root,bg="yellow",height=600,width=600)
'''
canvas.create_line(0,0,400,400,width=10,fill="red")
canvas.create_rectangle(100,100,400,400,width=10,fill="orange",outline="blue")
canvas.create_oval(100,100,300,400,width=10,fill="black",outline="blue")
points=[250,110,480,200,280,280,250,110]
canvas.create_polygon(points,fill="white")
canvas.create_arc(100,100,400,400,start=90, extent=150, fill="red")
'''

photo=PhotoImage(file="best.gif")
canvas.create_image(0,0,image=photo,anchor=NW)
canvas.pack()

root.geometry("800x800+320+200")
root.mainloop()