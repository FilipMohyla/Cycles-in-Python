from turtle import forward, left, right, shape, exitonclick, penup, pendown, pencolor

shape("turtle")

for h in range(4):
    for i in range(8-h):
        forward(45)
        left(360/(8-h))
   
    penup()
    forward(110)
    pendown()

exitonclick()