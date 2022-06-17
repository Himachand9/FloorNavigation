import turtle
from coordinates import Dict
from graph import graph
from shortest_path import find_shortest_path


w=turtle.Screen()
w.setup(1024,498)
w.setworldcoordinates(-512,-249,512,249)
w.register_shape("human.gif")
w.bgpic("pic.png")



A=w.textinput("Source Input", "Enter your current location :")
B=w.textinput("Destination Input", "Enter your final destination :")
A=A.upper()
B=B.upper()

anu=turtle.Turtle()
anu.shape("human.gif")
anu.pensize(4)
anu.turtlesize(0.4,0.4)
anu.penup()
l=(find_shortest_path(graph,A,B))

anu.shape("circle")
anu.goto(Dict[A])
anu.stamp()
anu.shape("human.gif")


for i in l:
    for key in Dict:
            
        if(key==i):
            anu.goto(Dict[key])
            anu.pendown()
            break

while(True):
    pass

