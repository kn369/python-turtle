#turtle graphics circle pattern

import turtle

turtle.colormode(255)
turtle.speed(100)
turtle.bgcolor("black")

color=["white","#900060","#905060","#505090","orange","yellow"]

def first_ring(c):
    turtle.color(color[c])
    for x in range(10):
        turtle.circle(175-5*x)

def primary_loop(c):
    for x in range(10):
        first_ring(c)
        turtle.rt(36)

def main():
    for x in range(4):
        primary_loop(x)
        turtle.rt(20)

main()
