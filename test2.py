def func(*a):
	print(a[0])
	max1,index=a[0],0
	for i in range(len(a)):
		#print("hello")
		if(max1<a[i]):
			max1,index=a[i],i
	max2=a[0]
	for i in range(len(a)):
		if(max2<a[i] and index!=i):
			max2,index=a[i],i
	if(len(a)<2):
		return max1,max1,len(a)
	else:
		return max1,max2,len(a)

max1,max2,count=func(1,3,2)
print(max1,max2,count)