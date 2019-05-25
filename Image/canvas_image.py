from tkinter import *

# create the canvas, size in pixels
canvas = Canvas(width=300, height=200, bg='white')

# pack the canvas into a frame/form
canvas.pack(expand=YES, fill=BOTH)

# load the .gif image file
gif1 = PhotoImage(file='Lenna.png')

# put gif image on canvas
# pic's upper left corner (NW) on the canvas is at x=50 y=10
canvas.create_image(50, 10, image=gif1, anchor=NW)
canvas.create_line(0,20,50,20)
# run it ...+++
mainloop()
