import turtle as t
import random as r

class Game():
    def turn_left(self):
        if t.heading() < 120:
            t.left(2)
    
    def turn_right(self):
        if t.heading() > 60:
            t.right(2)

    def fire(self):
        ang = t.heading()

        while t.ycor() < 150:
            t.forward(15)

        d = t.distance(target, 150)

        if d < 15:
            t.goto(0,0)
            t.color("blue")
            t.write("잡았어요!", False, "center", ("", 20))
        else:
            t.color("red")
            t.write("다시 도전해요.", False, "center", ("", 10))

        t.color("black")
        t.goto(0, -140)
        t.setheading(ang)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()


go(-150,-150)
t.forward(300)


go (-150,150)
t.color("skyblue")
t.forward(300)


target = r.randint(-150,150)


t.pensize(2)
t.color("blue")
go(target-10,150)


t.begin_fill


for i in range(3):
    t.forward(20)
    t.left(120)


t.end_fill


t.color("black")
t.up()
t.goto(0,-140)
t.setheading(90)


g=Game()


t.onkeypress(g.turn_right,"Right")
t.onkeypress(g.turn_left,"Left")
t.onkeypress(g.fire,"space")
t.listen()

t.done()