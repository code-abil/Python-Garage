from tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

def say():
    print("entry_1 Command executed")

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master,selectforeground='red',selectbackground='yellow')
e2 = Entry(master, show="*")

e3 = Entry(master, state='disabled')
e4 = Entry(master,width=5)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2)
e4.grid(row=2,column=2)





mainloop( )
