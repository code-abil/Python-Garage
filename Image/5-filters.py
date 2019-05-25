from PIL import Image, ImageFilter

im = Image.open("Lenna.png")


im1 = im.filter(ImageFilter.CONTOUR)
im1.save("lenna_CONTOUR" + ".png")
im1.show()
#im1.show()

im1 = im.filter(ImageFilter.EMBOSS)
im1.save("lenna_EMBOSS" + ".png")
im1.show()
#im1.show()

im1 = im.filter(ImageFilter.FIND_EDGES)
im1.save("lenna_FINDEDGE" + ".png")
im1.show()
#im1.show()


from tkinter import *
window = Tk() 
window.title('Image Display')

f1 = Frame(window) 
f1.pack() 
f2 = Frame(window) 
f2.pack( side = BOTTOM )

l1 = Label(f1)
photo1=PhotoImage(file="Lenna_CONTOUR.png")
l1.config(image=photo1)
l1.pack()
 
l2 = Label(f2)
photo2=PhotoImage(file="Lenna_EMBOSS.png")
l2.config(image=photo2)
l2.pack()


