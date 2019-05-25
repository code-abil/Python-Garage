from tkinter import *

def show_entry_fields():
   s.set(e2.get())
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

s=StringVar()
e1 = Entry(master,textvar=s)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


#Setting default values
e1.insert(0,"abc")
e1.insert(5,"zzzzzzzzzz")
e2.insert(2,'asdasd')
e1.insert(0,"Miller")


Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=E)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=E)

mainloop( )
