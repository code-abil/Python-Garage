# from tkinter import *
# window=Tk()
# can=Canvas(window,bg="red",height=200,width=200)
# can.create_line(0,0,100,200)
# can.create_arc(0,0,5)
# can.pack()
# window.mainloop()


# from tkinter import *
# window=Tk()
# f1=Frame(window,bg="red",height=100,width=100)
# f1.pack(side=BOTTOM)
# label1=Label(f1,text="super cool")
# label1.pack()
# f2=Frame(window,bg="blue",height=100,width=100)
# f2.pack(side=TOP)
# window.mainloop()

def func(a):
    print(a)
from tkinter import *
window=Tk()
b=Button(window,command=lambda:func(2)).pack()
# f1=Frame(window,bg="red",height=100,width=100)
# f1.place(height=100,width=100)
# # label1=Label(f1,text="super cool")
# # label1.pack()
# f2=Frame(window,bg="blue",height=10,width=10)
# f2.place(height=200,width=200)
window.mainloop()