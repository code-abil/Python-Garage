def func (a):
	f=open(a,'r')
	print(f)
	#print(type(f.read()))
	#print(f.read())
	print(f.readlines())
	#f.write("This is Sparta.")
	f.close()
	#f=open(a,'w')
	#f.write("What the fuck")
	#print(type(f.readline()))
	#print(f.readline())
	#f.close()
# read 

func("oc.txt")

#f=open("doc.txt",'a')
#f.append("This is awesome")
#f.write("This is really cool")

#for i in f:
#	print(i)