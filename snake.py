import turtle
import time
import random

wn = turtle.Screen()
wn.title("a")
wn.bgcolor("green")

wn.setup(width=600, height=600)
wn.tracer(0)

a = turtle.Turtle()
a.speed(0)
a.shape("circle")
a.color("black")
a.penup()
a.goto(0,0)
a.direction = "stop"

def goup():
    if a.direction != "down":
        a.direction = "up"

def godown():
    if a.direction != "up":
        a.direction = "down"

def goleft():
    if a.direction != "right":
        a.direction = "left"

def goright():
    if a.direction != "left":
        a.direction = "right"

def move():
    if a.direction == "up":
        y = a.ycor()
        a.sety(y + 20)
    if a.direction == "down":
        y = a.ycor()
        a.sety(y - 20)
    if a.direction == "left":
        x = a.xcor()
        a.setx(x - 20)
    if a.direction == "right":
        x = a.xcor()
        a.setx(x + 20)

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []

while True:
    wn.update()
    if a.xcor()>290 or a.xcor()<-290 or a.ycor()>290 or a.ycor()<-290:
        time.sleep(1)
        a.goto(0,0)
        a.direction = "stop"
        colors = random.choise(['red', 'blue', 'green']) 
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

