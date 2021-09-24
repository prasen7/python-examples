import turtle
import time
import random

delay = 0.2

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Prasen")
wn.bgcolor("blue")
wn.setup(width=800, height=800)
wn. tracer(0)     # turns off the screen updates

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# fuctions
def go_up():
    if head.direction != "down":
        head.directon = "up"



def go_left():
    if head.direction != "right":
        head.directon = "left"

def go_right():
    if head.direction != "left":
        head.directon = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)        

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings- to connect a keypress to a particular job
wn.listen() #window to listen to keypress
wn.onkey(go_up, "w")
wn.onkey(go_down, "s")
wn.onkey(go_left, "a")
wn.onkey(go_right, "d")

#Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.shapesize(0.50, 0.50)
food.goto(0,100)

if head.distance(food)<15:
    # move the food to a random position on the screen
    x= random.randint(-290, 290)
    y= random.randint(-290, 290)
    food.goto(x, y)
# to increase the snake's body on touching the food
segments = []
#add a segment to the snake
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segments.append(new_segment)
# move the segment in reverse order
for index in range(len(segments)-1,0,-1):
    x=segments[index-1].xcor()
    y=segments[index-1].ycor()
    segments[index].goto(x, y)

# move segment 0 to where the head is
if len(segments) &amp;gt; 0:
    x = head.xcor()
    y = head.ycor()
    segments[0].goto(x, y)
#check fo collision
if head.xcor()> 290 or head.xcor()< -290 or head.ycor()>290 or head.ycor()<-290:
    time.sleep(1)
    head.goto(0,0)
    head.direction= "stop"
    for segment in segments:
        segment.goto(1000,1000)
        segments=[]

# check for head collision
for segment in segments:
    if segment.distance(head)<20:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000,1000)
            segment.clear()
# Add score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 Hogh Score: {}".format(high_score), align="center", font= ("Courier", 24, "normal"))
# Score
score=0
high_score=0            

# main game loop
while True:
    wn.update()

    move()

    time.sleep(delay)


wn.mainloop()