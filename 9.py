import sys
print("hi",sys.argv)
print(dir(sys))
s='sad'
print(sys.prefix)
try:
	a=5
	print(a/0)
except Exception as e:
	print("hello")
	print(sys.exc_info(),type(sys.exc_info()))


# print(sys.getallocatedblocks())
# l=[1,2,3,4,5,6]
# print(sys.getallocatedblocks())
# print(sys.getallocatedblocks())
# print(sys.getrefcount(l))
# print(l)
# s=l
# s=l
# a=l
# print(sys.getrefcount(l))
