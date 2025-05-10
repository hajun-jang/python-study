import turtle as t

def polygon(n,leng):   
    for i in range(n):
        t.forward(leng)
        t.left(360/n)

def parallel(leng,leng2,ang):
    for i in range(2):
        t.forward(leng)
        t.left(ang)
        t.forward(leng2)
        t.left(180-ang)
    
def trape(leng,leng2,leng3,ang):
    t.forward(leng)
    t.left(ang)
    t.forward(leng2)
    t.left(180-ang)
    t.forward(leng3)
    t.left(180-ang)
    t.forward(leng2)

def star(leng):
    for i in range(5):
        t.forward(leng)
        t.right(144)
        t.forward(leng)
        t.left(72)
    
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

go(-200,0)
polygon(4,30)
go(-100,0)
parallel(50,30,70)
go(50,0)
trape(70,30,60,100)
go(200,25)
t.setheading(0)
star(15)

t.done()