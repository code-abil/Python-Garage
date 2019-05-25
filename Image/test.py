from tkinter import *
from PIL import Image
win=Tk()
im=PhotoImage(file='Lenna.png')


fr=Frame(win,bg="red")
fr.pack()
lab=Label(win,bg="red")
lab.configure(image=im)
lab.pack(expand="yes")
win.mainloop()