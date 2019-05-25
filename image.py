from PIL import Image

'''try:
	#creates a image object
	im1=Image.open('cr7.jpg')
	im1.show()
	im1.save('cr7.png')
except:
	print("Image not found")'''


thumbnail_size=(50,50)

from os import *
#mkdir('thumbnails')
#print(getcwd())
#print(dir('as'))
#chdir('../')
#mkdir('png-folder')
#print(listdir())
# for file in listdir():
	
# 	if(file.endswith('.jpg')):
# 		image1=Image.open(file)
# 		#image1.show()
# 		# print(file)
# 		# file_name,file_extension=path.splitext(file)
# 		# print(path.splitext(file))
# 		# image1.save('./png-folder/{}.png'.format(file_name))
# 		# #print(file_name,file_extension)

# 		# #creating thumbnails in a folder of size 300*300	
# 		# image1.thumbnail(thumbnail_size)
# 		# #image1.show()
# 		# image1.save('thumbnails/{}_50.{}'.format(file_name,file_extension)) 
# 		roated_image=image1.rotate(90)
# 		roated_image.show()
# 		# image1.convert(mode='L')
# 		# image1.show()


from PIL.ImageFilter import *
image1=Image.open('cr7.jpg')
# image2=image1.resize((50,50))
# image2.show()
# print(image1.size)
image2=image1.crop((00,500,1000,1000))
image2.show()
image3=image2.resize((100,1000))
image3.show()
# filterd=image1.filter(GaussianBlur())
# filterd.show()
