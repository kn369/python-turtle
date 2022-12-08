import turtle
turtle.speed(1000)
turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()
for row in range(8):
    for column in range(8):
        if row%2==0 and column%2!=0:
            turtle.begin_fill()
        elif column%2==0 and row%2!=0:
            turtle.begin_fill()
        for x in range(4):
            turtle.fd(50)
            turtle.rt(90)
        turtle.end_fill()
        turtle.penup()
        turtle.fd(50)
        turtle.pendown()
    turtle.penup()
    turtle.goto(-200,-100)
    turtle.lt(90)
    y=(row+1)*50
    turtle.fd(y)
    turtle.rt(90)
    turtle.pendown()
