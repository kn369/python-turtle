import turtle

turtle.shape("turtle")
my_list=["blue","black","red","yellow","green"]
turtle.penup()
turtle.goto(-20,0)
turtle.pendown()
turtle.pensize(5)
for x in range(3):
    turtle.color(my_list[x])
    turtle.circle(50)
    turtle.penup()
    turtle.fd(115)
    turtle.pendown()
turtle.penup()
turtle.goto(0,0)
turtle.fd(38)
turtle.lt(90)
turtle.bk(60)
turtle.pendown()
turtle.rt(90)

for x in range(2):
    turtle.color(my_list[x+3])
    turtle.circle(50)
    turtle.penup()
    turtle.fd(115)
    turtle.pendown()
