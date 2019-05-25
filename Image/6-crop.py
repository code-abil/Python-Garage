
from PIL import Image, ImageFilter
try:
    im = Image.open("Lenna.png")
except:
    print ("Unable to load image")
    
box = (0, 0, 100,100)
cropped_image = im.crop(box)
cropped_image.show()
cropped_image.save('cropped_image.jpg')
