
from tkinter import *
r = Tk() 
r.geometry('300x500')
r.title('Counting Seconds') 
b = Button(r, text='Stop', width=20, command=r.destroy)


photo=PhotoImage(file="2.png")

b.config(image=photo)

#b.config(activebackground="red",bg="yellow" )


b.pack() 
r.mainloop() 
