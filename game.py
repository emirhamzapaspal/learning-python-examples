import turtle
import time
import random

speed = 0.15


wn = turtle.Screen()
wn.title("Snake game")
wn.bgcolor("lightgreen")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 100)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 0)
food.shapesize(0.80, 0.80)

tails = []
score = 0

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
pen.hideturtle()
pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


def goUp():
    if head.direction != "down":
        head.direction = "up"

def goDown():
    if head.direction != "up":
        head.direction = "down"

def goRight():
    if head.direction != "left":
        head.direction = "right"

def goLeft():
    if head.direction != "right":
        head.direction = "left"

stop = False

def change():
    global stop
    if stop == True:
        stop = False
    else:
        stop = True

wn.listen()
wn.onkey(goUp, "w")
wn.onkey(goDown, "s")
wn.onkey(goRight, "d")
wn.onkey(goLeft, "a")
wn.onkey(change, "p")

while True:
    wn.update()

    if not stop:

        if head.xcor() > 300 or head.xcor() < - 300 or head.ycor() > 300 or head.ycor() < -300:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for tail in tails:
                tail.goto(1000, 1000)

            tails = []
            score = 0
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            speed = 0.15

        if head.distance(food) < 20:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            food.goto(x, y)

            score = score + 1
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

            speed = speed - 0.001

            newtail = turtle.Turtle()
            newtail.speed(0)
            newtail.shape("square")
            newtail.color("white")
            newtail.penup()
            tails.append(newtail)

        for i in range(len(tails) - 1, 0, -1):
            x = tails[i - 1].xcor()
            y = tails[i - 1].ycor()
            tails[i].goto(x, y)

        if len(tails) > 0:
            x = head.xcor()
            y = head.ycor()
            tails[0].goto(x, y)
        
        move()
        time.sleep(speed)