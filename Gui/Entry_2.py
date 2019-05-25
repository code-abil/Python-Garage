from tkinter import *
from math import *

    
w = Tk()
Label(w, text="Your Expression:").pack()

entry = Entry(w)
entry.pack()

l = Label(w)
l.pack()

def evaluate(event):
    l.configure(text = "Your Result: " + str(eval(entry.get())))

entry.bind("<Return>", evaluate)

w.mainloop()
