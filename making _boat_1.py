import turtle as t

class Figure():
    num=0
    angle=0
    length=0
    length2=0
    length3=0

    def polygon(self):
        n=self.num
        leng=self.length
        for i in range(n):
            t.forward(leng)
            t.left(360/n)

    def parallel(self):
        leng=self.length
        leng2=self.length2
        ang=self.angle
        for i in range(2):
            t.forward(leng)
            t.left(ang)
            t.forward(leng2)
            t.left(180-ang)

    def trape(self):
        leng=self.lengh
        leng2=self.lengh2
        leng3=self.lengh3
        ang=self.angle
        t.forward(leng)
        t.left(ang)
        t.forward(leng2)
        t.left(180-ang)
        t.forward(leng3)
        t.left(180-ang)
        t.forward(leng2)

    def star(self):
        leng=self.length
        for i in range(5):
            t.forward(leng)
            t.right(144)
            t.forward(leng)
            t.left(72)


class Boat(Figure):
    def log(self):
        leng=self.length
        t.circle(leng/2)
        t.forward(leng*4)
        t.left(90)
        t.forward(leng)
        t.left(90)
        t.forward(leng*4)
        t.left(180)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

b = Boat()
b.num = 3
b.length = 50

for i in [0,-50,-100]:
    go(-100, i)
    b.log()

go(0, -25)
t.left(90)
t.forward(b.length*4)
t.left(180)

b.polygon()

t.left(90)
go(15, 150)
b.length = 7
b.star()
go(0,0)

t.done()