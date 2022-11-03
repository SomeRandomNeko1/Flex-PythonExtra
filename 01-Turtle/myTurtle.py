import turtle             
my_wn = turtle.Screen()
turtle.speed(11)
for b in range(30):
   turtle.circle(5*b)
   turtle.circle(-5*b)
   turtle.left(b)
turtle.exitonclick()