from PIL import Image, ImageFilter
try:
    original = Image.open("Lenna.png")
except:
    print ("Unable to load image")
print ("The size of the Image is: ")
print(original.format, original.size, original.mode)

#change type

original.save("Lenna_bmp.bmp")
original.show()
#resize

new_image = original.resize((200, 200))
new_image.save('lenna_400.jpg')
print(new_image.size)


