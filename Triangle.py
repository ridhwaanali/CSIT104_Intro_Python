#quadrant 1
def blanks(n):
    for i in range(2):
        print(" ",end="")

def starline(a):
    for i in range(a):
        print("*",end="")

def pp():
    for k in range(7):
        blanks(22-k)
        starline(5-k)
        print()

#main
pp()

#4th Quadrant
def blanks(n):
    for i in range(2):
        print(" ",end="")

def starline(a):
    for i in range(a):
        print("*",end="")

def pp():
    for k in range(7):
        blanks(22+k)
        starline(1+k)
        print()



#main
pp()

 
#quadrat 3
def blanks(n):
    for i in range(n):
        print(" ",end="")

def starline(a):
    for i in range(a):
        print("*",end="")

def pp():
    for k in range(10):
        blanks(22-k)
        starline(1+k)
        print()


#main
pp()

#quadrat 2
def blanks(n):
    for i in range(n):
        print(" ",end="")

def starline(n):
    for i in range(n):
        print("*",end="")

def pp():
    for k in range(10):
        blanks(22+k)
        starline(8-k)
        print()


#main
pp()
