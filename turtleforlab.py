import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['green']
for number in range(320):
    t.forward(number+12)
    t.right(83)
    t.pencolor(colors[number%1])
turtle.done()