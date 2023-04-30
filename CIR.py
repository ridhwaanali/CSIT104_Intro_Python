import math
import turtle

v=turtle.Turtle()
t=turtle.Turtle()

def init():
    t.hideturtle()
    v.hideturtle()
    t.penup()
    t.setpos(0,bot)
    t.pendown()
    t.shape('circle')
    v.penup()
    v.setpos(0,bot)
    v.pendown()
    v.shape('circle')
    v.pencolor('white')
    t.pencolor('red')
    t.pensize(size)
    v.pensize(size)
    t.speed('fast')
    v.speed('fast')
def up():
    for k in range(rang):
        t.sety(bot + inc*k)
        v.sety(bot + (inc * k - size))
def down():
         for k in range(rang):
            t.sety(top - inc*k)
            v.sety(top- (inc*k - size))
size=20
speed='fast'
top=200
bot=-top
inc=5
rang=int(2*top/inc)

init()
while True:
    up()
    down()
