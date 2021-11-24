from tkinter import *
root=Tk()

def open():
    print("file is opened")
main_menu=Menu(root)
root.config(menu=main_menu)

#file menu
file_menu=Menu(main_menu,tearoff=False)
main_menu.add_cascade(label="FILE",menu=file_menu)
file_menu.add_command(label="NEW",font=("Comic Sans MS",15,'bold'),accelerator="CTRL+N", command=open)
file_menu.add_separator()
file_menu.add_command(label="OPEN",accelerator="CTRL+O",command=open)
file_menu.add_command(label="SAVE",command=open)
#edit menu
edit_menu=Menu(main_menu)
main_menu.add_cascade(label="EDIT",menu=edit_menu)

txt=Text(root)
txt.pack(fill=BOTH,expand=1)
root.geometry("400x400+320+200")
root.mainloop()