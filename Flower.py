from turtle import forward, penup, pendown, circle, exitonclick, left, right, pencolor, pensize, speed, begin_fill, end_fill, fillcolor

speed(10)

penup()
right(90)
forward(350)
pendown()
right(180)
pencolor("LimeGreen")
pensize(3)
forward(70)
right(90)

begin_fill()
fillcolor("green")
for g in range(3):
    for h in range(1):
               
        for i in range(1, 20):
            left(3)
            forward(i)
            
            
        left(123)
       
        for j in range(1, 20):
            left(3)
            forward(j)
            
        
        right(147)
        forward(50)
        left(90)
		
        for k in range(1, 20):
            right(3)
            forward(k)
            
            
        right(123)
       
        for l in range(1, 20):
            right(3)
            forward(l)
    
    
    left(147)
    forward(50)
    right(90) 

    
end_fill()

left(90)
forward(150)

pencolor("Gold")
pensize(2)


begin_fill()
fillcolor("yellow")
for o in range(18):
    for p in range(4):
        forward(80)
        left(90)

    left(20)
end_fill()



exitonclick()