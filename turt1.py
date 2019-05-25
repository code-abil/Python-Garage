import turtle
win=turtle.Screen()

turt=turtle.Turtle()

turt.fillcolor('yellow')
turt.begin_fill()
for i in range(4):
	turt.forward(100)
	#turt.backward(100)
	turt.right(90)
turt.end_fill()
turt.penup()
turt.forward(500)
turt.pendown()
turt.color('blue')
turt.backward(500)
print(turt.position())
win.mainloop()