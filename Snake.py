import turtle
import time
import random

current_score = 0
highscore = 0
delay = 0.1

screen = turtle.Screen()
screen.title("Snake")
screen.setup(1000, 600)
screen.bgcolor("green")
screen.tracer(0)

turtle.color("light green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-450, 250)
turtle.pendown()
turtle.goto(450, 250)
turtle.goto(450, -250)
turtle.goto(-450, -250)
turtle.goto(-450, 250)
turtle.end_fill()
turtle.hideturtle()

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.penup()
head.goto(-340, 0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 0)

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Score: 0   Highscore: 0", align="center", font=("Courier", 25, "bold"))


def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def right():
    if head.direction != "left":
        head.direction = "right"


def left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)


mode = screen.textinput("mode", "easy or hard?")
screen.listen()
screen.onkeypress(up, "Up")
screen.onkeypress(down, "Down")
screen.onkeypress(right, "Right")
screen.onkeypress(left, "Left")
body = []

turtle.color("light blue") if mode == "easy" else turtle.color("red")
turtle.begin_fill()
turtle.penup()
turtle.goto(-450, 290)
turtle.pendown()
turtle.goto(-350, 290)
turtle.goto(-350, 255)
turtle.goto(-450, 255)
turtle.goto(-450, 290)
turtle.end_fill()
turtle.hideturtle()
turtle.goto(-400, 255)
turtle.color("black")
turtle.write("EASY", align="center", font=("Courier", 25, "bold")) if mode == "easy" else turtle.write("HARD", align="center", font=("Courier", 25, "bold"))
while True:
    screen.update()
    if mode == "hard":
        if head.ycor() > 240 or head.ycor() < -240 or head.xcor() > 440 or head.xcor() < -440:
            time.sleep(1)
            head.goto(-350, 0)
            head.direction = "stop"
            food.goto(0, 0)
            for i in body:
                i.goto(1000, 1000)
            body.clear()
            current_score = 0
            score.clear()
            score.write(f"Score: {current_score}   Highscore: {highscore}", align="center", font=("Courier", 25, "bold"))
    else:
        if head.ycor() > 240:
            head.sety(-240)
        if head.ycor() < -240:
            head.sety(240)
        if head.xcor() > 440:
            head.setx(-440)
        if head.xcor() < -440:
            head.setx(440)

    if head.distance(food) < 20:
        food.goto(random.randint(-440, 440), random.randint(-240, 240))
        if mode == "hard":
            delay -= 0.001
        else:
            delay = 0.1
        tail = turtle.Turtle()
        tail.speed(0)
        tail.shape("circle")
        tail.color("blue")
        tail.penup()
        body.append(tail)

        current_score += 1
        if current_score > highscore:
            highscore = current_score
        score.clear()
        score.write(f"Score: {current_score}   Highscore: {highscore}", align="center", font=("Courier", 25, "bold"))

    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        body[0].goto(head.xcor(), head.ycor())
    move()
    for i in body:
        if i.distance(head) < 20:
            time.sleep(1)
            head.goto(-350, 0)
            head.direction = "stop"
            food.goto(0, 0)
            for n in body:
                n.goto(1000, 1000)
            body.clear()
            current_score = 0
            score.clear()
            score.write(f"Score: {current_score}   Highscore: {highscore}", align="center", font=("Courier", 25, "bold"))
        if i.distance(food) < 20:
            food.goto(random.randint(-440, 440), random.randint(-240, 240))

    time.sleep(delay)
