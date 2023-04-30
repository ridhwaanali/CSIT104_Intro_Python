import turtle
t=turtle.Turtle()
def frame():
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)  
    t.forward(200)
frame()

def drawOne(x,y):
    t.penup()
    t.setpos(x,y)
    t.left(90)
    t.pendown()
    t.fd(50)
    t.penup()
    t.home()

def drawZero(x,y):
    t.penup()
    t.setpos(x,y)
    t.left(90)
    t.pendown()
    t.circle(20)
    t.penup()
    t.home()

def drawQuadThree():
    drawZero(50,50)
    drawZero(90,50)

def drawQuadFour():
    drawZero(180,50)
    drawOne(130,30)
def drawQuadOne():
    drawOne(180,130)
    drawOne(150,130)
def drawQuadTwo():
    drawOne(65,130)
    drawZero(50,150)

#main


drawQuadThree()
drawQuadFour()
drawQuadOne()
drawQuadTwo()
