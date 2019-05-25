from PIL import Image

size = (128, 128)

try:
    im =  Image.open("Lenna.png")
except:
    print ("Unable to load image")

im.thumbnail(size)
im.save('lenna_thumbn.jpg')
im.show()
