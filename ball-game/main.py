import turtle
import random
import math

# Defining screen
screen = turtle.Screen()
screen.setup(400, 400)
#screen.bgcolor((135, 206, 250))
screen.addshape("images/ball.gif")
screen.addshape("images/exploded_ball.gif")
screen.addshape("images/line1.gif")

# Defining objects
ball = turtle.Turtle()
ball.shape("images/ball.gif")

pad = turtle.Turtle()
pad.shape("images/line1.gif")

scoreKeeper = turtle.Turtle()
levelObj = turtle.Turtle()

# Initializing objects
ball.penup()
ball.speed(0)

pad.penup()
pad.speed(0)

pad.setx(100)
pad.sety(-190)
pad.right(90)

scoreKeeper.penup()
scoreKeeper.hideturtle()
scoreKeeper.setx(50)
scoreKeeper.sety(180)
style = ('Courier', 12, 'bold')

levelObj.penup()
levelObj.hideturtle()
levelObj.setx(-100)
levelObj.sety(180)


# a function to move pad left by 20 pixels
def _left():
    corx = pad.xcor() - 20
    pad.setx(corx);


# a function to move pad right by 20 pixels

def _right():
    pad.setx(pad.xcor() + 20)


# Defining left key and right key to move the pad
screen.onkey(_left, "Left")
screen.onkey(_right, "Right")

screen.listen()

game_level = 1
speed = 0
score = 0
scoreKeeper.clear()
scoreKeeper.write("Score: %d" % (score), font=style)

levelObj.clear()
levelObj.write("Level: %d" % (game_level), font=style)

# Main loop
while (True):
    if score == 10:
        score = 0
        game_level = game_level + 1
        speed = speed + 2
        levelObj.clear()
        levelObj.write("Level: %d" % (game_level), font=style)

    ystep = -speed
    ball.sety(200)  # initial height of the ball
    ball.shape("images/ball.gif")
    ball.setx(random.randint(-180, 180))  # set x position to random value
    xstep = random.randint(-5, 5)
    lost = False

    while (ball.ycor() > -200):  # As long as the ball in the air
        ystep = ystep - 0.2  # add acceleration due to gravity
        if ((ball.ycor() > 190) & (ystep > 0)):
            break  # exit when the ball reaches the ceiling and restart
        if ((ball.ycor() < -170) & (ystep < 0) & (lost == False)):  # if the ball is on the floor level and is falling
            if (abs(
                    ball.xcor() - pad.xcor()) > 30):  # if the ball position is different from the pad position by more than 30 pixels
                scoreKeeper.clear()
                scoreKeeper.color("Red")
                score = score - 1
                ball.shape("images/exploded_ball.gif")
                lost = True
            else:
                scoreKeeper.clear()
                scoreKeeper.color("Black")
                score = score + 1
                ystep = -ystep * 0.9
            scoreKeeper.write("Score: %d" % (score), font=style)
        if (lost == False):  # Rotate only a ball,but not the exploded ball
            ball.right(7)

        ball.setx(ball.xcor() + xstep)
        ball.sety(ball.ycor() + round(ystep))

        if (abs(ball.xcor()) > 180):
            xstep = -xstep


