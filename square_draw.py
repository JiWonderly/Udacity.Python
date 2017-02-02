import turtle


def draw_geometric_figures():
  
    window = turtle.Screen()
    window.bgcolor("red")

    

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("white")
    brad.speed(2)

    i = 0
    
    for i in range(4):
      brad.forward(100)
      brad.right(90)

      


    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    
    #jiwon = turtle.Turtle()
    #jiwon.shape("turtle")
    jiwon.color("yellow")
    
    
    #num_sides = 3
    #side_length = 70
    #angle = 360.0/num_sides

    #for j in range(num_sides):
      #jiwon.forward(side_length)
      #jiwon.left(angle)
     
       

     
    
    window.exitonclick()
    
  
draw_geometric_figures() 
