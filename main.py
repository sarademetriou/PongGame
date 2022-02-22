import turtle

wn = turtle.Screen()
wn.title("Pong by Sarra")
wn.bgcolor("light yellow")
wn.setup(width=800, height=600)
wn.tracer()

#SCORE!
score_a = 0
score_b = 0



#Paddle A

#we need to name this paddle
paddle_a = turtle.Turtle()
#small t because thats the module name (what we imported)
#T bc thats the class name.
paddle_a.speed(0)
paddle_a.shape("square")   #20x20 pixels so we want to stretch this shape.
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("pink")
paddle_a.penup()
paddle_a.goto(-350, 0)



#Paddle B

paddle_b = turtle.Turtle()

paddle_b.speed(0)
paddle_b.shape("square")   #20x20 pixels so we want to stretch this shape.
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("pink")
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()

ball.speed(0)
ball.shape("circle")   #20x20 pixels so we want to stretch this shape.
#paddle_b.shapesize(stretch_wid=5, stretch_len=1)
ball.color("light blue")
ball.penup()
ball.goto(0, 0)


ball.dx = 4
ball.dy = 4 # 2 pixels


#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("Pink")
pen.penup()
pen.hideturtle()
pen.goto (0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))




# functions: we have to define the function for the different movements: paddle a for up and down, p.b up and down.

#we are going to define the coord y as paddlea(y coordinate) ycor is from turtle module and returns the y coord.
# we assign this to a variable called y
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    # this means to move the y coord up by a pixel of 20 upwards
    paddle_a.sety(y)
# we are setting the paddle y coord to the new y coord (the one where we add 2 pixels when we go up)

 # above we defined the function, now we call the function:

#keyboard binding:
wn.listen()
wn.onkeypress(paddle_a_up, "w")
# so needs to lsiten to the keyboard input, w moves the paddle up by the 20 pxls





def paddle_a_up():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "s")


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_b_up, "Up")

def paddle_b_up():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_b_up, "Down")

# Main Game Loop

while True:
    wn.update()

#now we need to move the ball in here:
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#set so ball stays in border:

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()

        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #now do coords of paddle and ball


#paddle and bal collisions:

    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1





