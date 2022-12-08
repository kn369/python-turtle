import turtle
from random import *

turtle.shape("turtle")
satyam=turtle.clone()
shivam=satyam.clone()
sundaram=turtle.clone()
shuradam=turtle.clone()
turtle.speed(20)
turtle.ht()

#for satyam
satyam.color("purple")
satyam.penup()
satyam.goto(-250,200)
satyam.speed(20)

#for shivam
shivam.color("blue")
shivam.penup()
shivam.goto(-250,150)
shivam.speed(20)

#for sundaram
sundaram.color("green")
sundaram.penup()
sundaram.goto(-250,100)
sundaram.speed(20)

#for shuradam
shuradam.color("red")
shuradam.penup()
shuradam.goto(-250,50)
shuradam.speed(20)

#for track
turtle.penup()
turtle.goto(-250,250)
turtle.pendown()
turtle.fd(500)
turtle.goto(-200,250)
for x in range(10):
    turtle.lt(90)
    turtle.bk(250)
    turtle.fd(250)
    turtle.rt(90)
    turtle.fd(50)
turtle.color("white")
turtle.bk(550) 

#turtle spin
for x in range(15):
    satyam.rt(24)
    shivam.rt(24)
    sundaram.rt(24)
    shuradam.rt(24)

#for race
for x in range(160):
    satyam.fd(randint(2,4))
    shivam.fd(randint(2,4))
    sundaram.fd(randint(2,4))
    shuradam.fd(randint(2,4))
    satyam_pos=satyam.xcor()
    shivam_pos=shivam.xcor()
    sundaram_pos=sundaram.xcor()
    shuradam_pos=shuradam.xcor()

List=[satyam_pos,shivam_pos,sundaram_pos,shuradam_pos]
print(List)
if max(List)==satyam.xcor():
    satyam.write("I am winner")
elif max(List)==shivam.xcor():
    shivam.write("I am winner")
elif max(List)==sundaram.xcor():
    sundaram.write("I am winner")
else:
    shuradam.write("I am winner")








