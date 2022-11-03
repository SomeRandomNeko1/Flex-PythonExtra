from ast import arg
import turtle
turtle.setup



def driehoek():

    turtle.fillcolor("Yellow")
    turtle.begin_fill()

    turtle.width(15) 

    turtle.color("yellow")
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100)
    turtle.left(120)
    turtle.forward(100) 

    turtle.penup()
    turtle.right(150)
    turtle.forward(50)

    turtle.color("yellow")
    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(120)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(100)

    turtle.left(120)
    turtle.left(90)
    turtle.left(30)
    turtle.forward(100)
    turtle.left(90)
    turtle.left(90)
    turtle.left(30)
    turtle.left(30)
    

    turtle.end_fill()
driehoek() 
input()