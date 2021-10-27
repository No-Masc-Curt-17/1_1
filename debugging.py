import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

def circles():
    radius = 100
    color_choice = input(("What color would you like?"))
    for i in range(4):
        painter.begin_fill()
        painter.fillcolor(color_choice)
        painter.penup()
        painter.goto(0,-radius)
        painter.pendown()
        painter.circle(radius)
        painter.end_fill()
        radius -= 25
        color_choice = input(("What color would you like?"))
        
circles()
    
    