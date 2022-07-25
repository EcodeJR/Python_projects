import turtle
colours = ["red", "blue", "green", "yellow", "purple", "orange"]
t = turtle.Turtle()
turtle.speed(10)
turtle.bgcolor("black")
for i in range(200):
    t = turtle.color(colours[i%6])
    t = turtle.width(i/100+1)
    t = turtle.forward(i)
    t = turtle.left(59)