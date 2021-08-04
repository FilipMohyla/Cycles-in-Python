from turtle import forward, left, right, shape, exitonclick, penup, pendown, pencolor, circle, speed

shape("turtle")
speed(10)

for i in range(67):
    left(45)
    forward(i*1.5) 

exitonclick()