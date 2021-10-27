import turtle as trtl

painter = trtl.Turtle()


painter.rt(45)
painter.begin_fill()
painter.fillcolor("red")
for i in range(3):
  painter.fd(30)
  painter.lt(120)
  
painter.end_fill()