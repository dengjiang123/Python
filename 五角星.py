from turtle import *
setup(1.0,1.0,0,0)
speed(10)
penup()
forward(200)
right(90)
forward(200)
left(90)
pendown()
def abc():
	begin_fill()
	color("red")
	for i in range(5):
		forward(100)
		right(144)
	end_fill()

for i in range(10):
	abc()
	penup()
	left(36)
	forward(50)
	pendown()

x=input()