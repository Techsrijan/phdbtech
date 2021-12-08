from tkinter import *
from PIL import Image,ImageTk
def msg():
    print("video is playing")
root=Tk()


play_image=ImageTk.PhotoImage(Image.open('images/playButton.png'))
btn=Button(root,image=play_image,command=msg)
btn.pack()

root.geometry("800x500+150+120")
root.mainloop()