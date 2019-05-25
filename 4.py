# s="{}kljnasldk{}".format('abilas',1);
# # Curly braces are called Place Holders.
# print(s)

# s="{1}    {0}".format('abilas',1);
# print(s)

# d={'name':'Abilash','age':18}
# print(d['name'])
# s="Name is {0},and age is {1}".format(d['name'],d['age'])
# print(s)


# #IMportantttttttttt
# s="name is {0[name]} and age is {0[age]}".format(d)
# print(s)


# #Keyword Arguments
# s="name is {name} but age is {age}".format(age=10,name='abilasj')
# print(s)

# #Important
# d={'name':'Abilash','age':18,'name':'kalyani'}	
# print(d)

# #d={.5:'Woow',[1,2]:'aweosme'}
# #Key of a dictionary cant be mutable.

# d=dict([(1,2),(2,(3,4))])
# print(d)

# d={}
# d[0]=5
# d[0]=1,2,3
# x=1,2,3
# d[0]=d[0]+(4,)		#Whenever we concatenate ,we have to concatenate two similar types of object
# print(type(x))		#python automatically considers as a tuple
# print(d)


# x=(4)#This is an integer
# x=(4,)#this is a tuple
# print(type(x))

# d={'name':'Abilash',"age":10}
# print(d.get('name'))      # if a particular key is not found,it returns none ,instead of raising an exception
# print(type(d.get('ame')))

# d={}
# s="Abilashh"
# for i in s:
# 	if i not in d:
# 		d[i]=1
# 	else:
# 	 	d[i]+=1
# for i in d:
# 	print(i,d[i])

# s='Abilash'
# y="Abilash"
# print(id(s),id(y))

# l1=(1)
# l2=()
# print(type(l1),type(l2))
# print(id(l1),id(l2))


# d={1:2,2:3,3:4}
# print(d)

# del d[3]
# print(d)

# d.clear()	#removes everything in dict
# print(d)

# del d
# #print(d) raises an error because dictionary got deleted
# s='as'
# print(s)
# del s
# #print(s)

# d={1:2,2:3,3:4}
# x=d.pop(1)	#retturns the value of key ,and then delete the pair
# print(x,d)

# # x=d.pop(4)	#raises an error,when not found
# # print(x)

# x=d.pop(4,'asdk')	#Doesnt raise an error, if key not found
# print(x)


# d={1:2}
# print(type(d.keys())) 	#returns a view object

# d.update({1:3,2:3})
# print(d)


# def fun(*a):		#packing args
# 	print(a,type(a))		# a will be a tuple
# fun(1,2,3)

# def fun(a,b,c):
# 	print(a,b,c)
# a=[1,2,3]
# fun(*a)	#unpacking

# def fun(*a):
# 	print('hi')

# fun(1,2,3)		#The later function declaration overrides the previous func declarations



# a=5;
# s='as'
# d={1:2,2:3,3:4}
# def func():
# 	print(s)		#we are trying to reference a local variable before assigning it
# 	a=10
# 	s='asdk'		#since we have a local variabel here, 
# 	print(a)
# func()
# print(a,s)



# a=4
# def fun():
# 	global a      #without this ,dunc will lead to error
# 	a=a+5
# 	print(a)
# fun()



# Python program showing a use of 
# global in nested function 

def add(): 
	x = 15
	
	def change(): 
		global x 
		x = 20
	print("Before making changing: ", x) 
	print("Making change") 
	change() 
	print("After making change: ", x) 

add() 
print("value of x",x) 
