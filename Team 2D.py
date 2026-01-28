import turtle

#Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(8)

#Outer gold ring
t.penup()
t.goto(140, 70)     # RIGHT (+x) and UP (+y)
t.setheading(110)    # Cut at 90 degrees (top)
t.pendown()

t.width(10)
t.pencolor("#d4a23a")
t.circle(150, 340)  # 270° arc → 90° gap
