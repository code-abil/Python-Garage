from tkinter import *

master = Tk()

a = StringVar()
e = Entry(master, textvariable=a)
e.pack()

a.set("helloooo...")
s = a.get()
print(s)
