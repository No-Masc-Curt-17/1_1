#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

y = -200
while (y < 200): 
  y = y + 50
  x = -200
  painter.goto(x,y)
  painter.color("purple")
  painter.stamp()
  while (x > 150):
    x = x + 50
    painter.goto(x,y)
    painter.color("orange")
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()