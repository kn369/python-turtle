import turtle

color=["red","yellow","green","blue","orange","purple","red","pink","yellow"]
for x in range(9):
    colour=color[x]
    turtle.color(colour)
    for y in range(2):
        turtle.fd(100)
        turtle.rt(60)
        turtle.fd(100)
        turtle.rt(120)
    turtle.goto(0,0)
    turtle.rt(40)
