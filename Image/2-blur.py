from PIL import Image , ImageFilter
try:
    # Load an image from the hard drive
    original = Image.open("Lenna.png")

    # Blur the image
    blurred = original.filter(ImageFilter.BLUR)
    blurred.show()
    #000 Display both images
    
    #original.show()
    #blurred.show()

    # save the new image
    blurred.save("blurred.png")

except:
    print ("Unable to load image")



from tkinter import *
window = Tk() 
window.title('Image Display')


# p=PhotoImage(file='Lenna.png') 
f1 = Frame(window)
f1.pack( side = RIGHT ) 
f2 = Frame(window) 
f2.pack()

l1 = Label(f1)
photo1=PhotoImage(file="Lenna.png")
l1.config(image=photo1)
#im=g.open("Lenna.png")
#l1.config(image=im)
l1.pack()
 
l2 = Label(f2)
photo2=PhotoImage(file="blurred.png")
l2.config(image=photo2)
l2.pack()



window.mainloop() 
