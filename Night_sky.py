from turtle import forward, left, right, shape, exitonclick, penup, pendown, pencolor, position, circle, speed, bgcolor,filling, fillcolor, begin_fill,end_fill
from random import randrange

shape("turtle")
bgcolor("black")

penup()
left(160)
forward(500)
right(160)
pendown()

### Start of drawing moon ###

for a in range(2):

    if a == 0:
        
        begin_fill()
        fillcolor("mintcream")
        circle(60)
        end_fill()
    else:
        
        begin_fill()
        fillcolor("black")
        circle(60)
        end_fill()
    
    for b in range(1):
        penup()
        forward(25)
        pendown()
        
### End of drawing moon ####

penup()
right(45)
forward(400)
left(45)

### Start of drawing stars ###

for b in range(1, 50):
    y = randrange(135)
    z = randrange(70, 120)
    x = randrange(15, 50)
    penup()
    left(y)
    forward(z)
    pendown()
    begin_fill()
    
    if b % 2 == 1:
        
        pencolor("WhiteSmoke")
        fillcolor("WhiteSmoke")     
    else:
        pencolor("yellow")
        fillcolor("yellow")
             
    for c in range(12):
        
        forward(x)
        left(360-150)
    
    end_fill()
    

### End of drawin stars ###


        
exitonclick()