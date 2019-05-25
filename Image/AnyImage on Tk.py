import tkinter as tk
from PIL import ImageTk, Image

#This creates the main window of an application
window = tk.Tk()
window.title("Join")
window.geometry("700x700")
#window.configure(background='grey')
window.bgcolor('grey')
im = Image.open("Lenna.png")
#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
photo = ImageTk.PhotoImage(im)


#Error, only gif,png,ppm/pgm
#img=tk.PhotoImage(file="")


#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(window, image = photo)



#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes")




#Start the GUI
window.mainloop()
