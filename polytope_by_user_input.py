from turtle import forward, left, right, shape, exitonclick, penup, pendown, pencolor

shape("turtle")

angle = int(input("Zadej počet úhlů n-úhelníku: "))

for i in range(angle):
    forward(45)
    left(360/angle)




exitonclick()