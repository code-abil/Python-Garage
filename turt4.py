import turtle
win=turtle.Screen()
turt=turtle.Turtle()
for i in range(6):
	turt.forward(100)
	turt.right(60)
turt.penup()
turt.goto(50,-100)
turt.pendown()
turt.circle(20)
win.mainloop()