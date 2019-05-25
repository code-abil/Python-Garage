from PIL import Image
import os

#path = "C:/Users/Desktop/python/images/"

path='image_dir'

dirs = os.listdir( path )


for item in dirs:
      #print(item)
      if os.path.isfile(path+'/'+item):
           if item.endswith('.jpg'):
                  im = Image.open(path+'/'+item)
                  f, e = os.path.splitext(item)
                  print(f,e)
                  imResize = im.resize((200,200), Image.ANTIALIAS)
                  #imResize.save(f + ' resized.jpg', 'JPEG')
                  imResize.save(path+'/200/{}{}'.format(f,e))
                  print(f)





dirs = os.listdir('.')

for item in dirs:
      #print(item)
      if os.path.isfile(item):
         if item.endswith('.jpg'):
            im = Image.open(item)
            f, e = os.path.splitext(item)
            imResize = im.resize((200,200), Image.ANTIALIAS)
            imResize.save(f+'_resized.jpg')
            
