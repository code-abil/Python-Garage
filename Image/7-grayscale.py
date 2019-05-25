from PIL import Image, ImageFilter
try:
    im = Image.open("Lenna.png")
except:
    print ("Unable to load image")

greyscale_image = im.convert('L')
greyscale_image.show()


greyscale_image = im.convert('CMYK')
greyscale_image.show()

greyscale_image.save('greyscale_image.jpg')
