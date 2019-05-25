f=open('CR7.jpg','rb')
print(f.read())
f.write(bytearray(1))
f.close()