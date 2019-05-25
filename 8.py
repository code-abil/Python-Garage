# a=5.0
# b=2.0
# print(a//b)
# a=5
# b=2
# print(a/b)

a=5
b=0
try:
	print(a/b)
except ZeroDivisionError:
	print("lola")
except Exception as e:
	print("Soory"+str(e))
	print(type(e))
finally:
	print("Awesome")

a=eval(input('Enter'))
print(type(a))
print(2**5)
import math
print(math.sqrt(9))