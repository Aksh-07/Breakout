import time
import turtle
from life import Live
from score import Score
from ball import Ball

s = turtle.Screen()
s.tracer(0)
s.setup(1000, 860)
s.bgcolor("black")
s.title("Breakout Game")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
a = 0
x_no = range(-480, 500, 60)
y_no = range(0, 300, 50)

b = turtle.Turtle()
b.penup()
b.setposition(-350, 350)
b.hideturtle()
b.color("white")
b.write("Total Lifes", font=("Courier", 40, "normal"))
board = Live(-300, 300)

c = turtle.Turtle()
c.penup()
c.setposition(300, 350)
c.hideturtle()
c.color("white")
c.write("Tiles", font=("Courier", 40, "normal"))
c_board = Score(350, 300)

game_is_on = True

tiles = []

for i in y_no:

    for j in x_no:
        r = turtle.Turtle()
        r.penup()
        r.speed(9)
        r.shape("square")
        r.color(colors[a])

        r.shapesize(1, 2)
        r.sety(i)
        r.setx(j)
        tiles.append(r)
    a += 1

bat = turtle.Turtle()
bat.penup()
bat.shape("square")
bat.shapesize(1, 4)
bat.color("white")
bat.setposition(0, -340)

ball = Ball()


def move_right():
    bat.fd(30)


def move_left():
    bat.bk(30)


s.listen()
s.onkey(move_right, "Right")
s.onkey(move_left, "Left")

while game_is_on:
    s.update()
    ball.starting_move()
    time.sleep(ball.ball_speed)

    if ball.xcor() > 490 or ball.xcor() < -490 or ball.ycor() > 380:
        ball.bounce_x()

    if ball.distance(bat) < 30:
        ball.bounce_y()

    if ball.ycor() < -345:
        ball.reset()
        board.del_live()

    for t in tiles:
        if ball.distance(t) < 20:
            t.hideturtle()
            ball.bounce_y()
            c_board.add_score()

    if board.lives == 0:
        board.game_over()
        break

s.exitonclick()
