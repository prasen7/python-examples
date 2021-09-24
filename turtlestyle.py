# turtle design
import turtle
turtle.pensize(2)
turtle.bgcolor('skyblue')
turtle.speed(0)

c=['red','brown','blue','white','yellow','orange','black','green','red','green']
for i in range(6):
    for colour in c:
        turtle.color(colour)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle()
    
