
import tkinter

window = tkinter.Tk()
window.title("GUI")
window.geometry('300x300')
# creating a function with an arguments 'event'
def say_hi(event): # you can rename 'event' to anything you want
    tkinter.Label(window, text = "Hi").pack()

# btn = tkinter.Button(window, text = "Click Me!")
window.bind("<Return>", say_hi) # 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
# btn.pack()

window.mainloop()  
