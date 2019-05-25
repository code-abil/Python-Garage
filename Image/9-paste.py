from PIL import Image, ImageFilter


image = Image.open('Lenna.png')
logo = Image.open('lenna_thumbn.jpg')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('pasted_image.jpg')
image_copy.show()
