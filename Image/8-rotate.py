from PIL import Image, ImageFilter
try:
    image = Image.open("Lenna.png")
except:
    print ("Unable to load image")
    

image_rot_90 = image.rotate(90)
image_rot_90.save('image_rot_90.jpg')
image_rot_90.show()

image_rot_180 = image.rotate(180)
image_rot_180.show()
image_rot_180.save('image_rot_180.jpg')



