import turtle
win=turtle.Screen()
turt=turtle.Turtle()

turt.forward(100)
print(turt.position())

print(turt.heading())
turt.fillcolor('red')
turt.begin_fill()
turt.circle(50)
turt.end_fill()
win.mainloop()