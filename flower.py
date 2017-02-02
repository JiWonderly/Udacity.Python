import turtle

def draw_flower(some_turtle):
    for i in range (1,5):
       some_turtle.forward(100) 
       some_turtle.right(90)
      
      
      
def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")

    jiwon = turtle.Turtle()
    jiwon.shape("arrow")
    jiwon.color("yellow")
    jiwon.speed(25)
    for i in range(1,75):
        draw_flower(jiwon)
        #jiwon.backward(20)
        jiwon.left(5)
    for i in range(30,31):
         jiwon.left(80)
         jiwon.backward(200)
       
    windows.exitonclock()

draw_art()    
 
