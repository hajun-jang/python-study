import turtle as t
import random as r

shark1 = t.Turtle()
shark1.shape("triangle")
shark1.color("red")
shark1.speed(0)
shark1.penup()
shark1.goto(r.randint(-1000,1000),r.randint(-650,650))


shark2 = t.Turtle()
shark2.shape("triangle")
shark2.color("yellow")
shark2.speed(0)
shark2.penup()
shark2.goto(r.randint(-1000,1000),r.randint(-650,650))


shark3 = t.Turtle()
shark3.shape("triangle")
shark3.color("blue")
shark3.speed(0)
shark3.penup()
shark3.goto(r.randint(-1000,1000),r.randint(-650,650))

shark4 = t.Turtle()
shark4.shape("triangle")
shark4.color("orange")
shark4.speed(0)
shark4.penup()
shark4.goto(r.randint(-1000,1000),r.randint(-650,650))

shark5 = t.Turtle()
shark5.shape("triangle")
shark5.color("purple")
shark5.speed(0)
shark5.penup()
shark5.goto(r.randint(-1000,1000),r.randint(-650,650))

shark6 = t.Turtle()
shark6.shape("square")
shark6.color("light green")
shark6.speed(0)
shark6.penup()
shark6.goto(r.randint(-1000,1000),r.randint(-650,650))


parts=t.Turtle()
parts.shape("circle")
parts.color("green")
parts.speed(0)
parts.penup()
parts.goto(r.randint(-1000,1000),r.randint(-650,650))


rock1=t.Turtle()
rock1.shape("circle")
rock1.color("green")
rock1.speed(0)
rock1.penup()
rock1.goto(r.randint(-1000,1000),r.randint(-650,650))


rock2=t.Turtle()
rock2.shape("circle")
rock2.color("green")
rock2.speed(0)
rock2.penup()
rock2.goto(r.randint(-1000,1000),r.randint(-650,650))

rock3=t.Turtle()
rock3.shape("circle")
rock3.color("green")
rock3.speed(0)
rock3.penup()
rock3.goto(r.randint(-1000,1000),r.randint(-650,650))

rock4=t.Turtle()
rock4.shape("circle")
rock4.color("green")
rock4.speed(0)
rock4.penup()
rock4.goto(r.randint(-1000,1000),r.randint(-650,650))

rock5=t.Turtle()
rock5.shape("circle")
rock5.color("green")
rock5.speed(0)
rock5.penup()
rock5.goto(r.randint(-1000,1000),r.randint(-650,650))

parts_map=t.Turtle()
parts_map.shape("circle")
parts_map.color("green")
parts_map.speed(0)
parts_map.penup()
parts_map.goto(r.randint(-1000,1000),r.randint(-650,650))

class Game():
    def turn_right(self):
        t.setheading(0)


    def turn_up(self):
        t.setheading(90)


    def turn_left(self):
        t.setheading(180)


    def turn_down(self):
        t.setheading(270)

    def parts_map_effect_done(self):
        parts.color("green")
        parts_map.ht()
        self.play()

    def play(self):
        t.clear()
        t.forward(16)


        ang=shark1.towards(t.pos())
        shark1.setheading(ang)
        shark1.forward(11)

        ang=shark2.towards(t.pos())
        shark2.setheading(ang)
        shark2.forward(14)

        ang=shark3.towards(t.pos())
        shark3.setheading(ang)
        shark3.forward(13)

        ang=shark4.towards(t.pos())
        shark4.setheading(ang)
        shark4.forward(12)

        ang=shark5.towards(t.pos())
        shark5.setheading(ang)
        shark5.forward(15)

        ang=shark6.towards(t.pos())
        shark6.setheading(ang)
        shark6.forward(10)

        ang=parts_map.towards(t.pos())
        parts_map.setheading(ang)
        parts_map.forward(0.1)



        duration=0


        if t.distance(parts)<15:
            self.result("부품을 찾았어요!",duration)
        elif t.distance(rock1)<15 or t.distance(rock2)<15 or t.distance(rock3)<15 or t.distance(rock4)<15 or t.distance(rock5)<15:
            duration=1
            self.result("암초였어요.",duration)
        elif t.distance(shark1)<15 or t.distance(shark2)<15 or t.distance(shark3)<15 or t.distance(shark4)<15 or t.distance(shark5)<15:
            self.result("다시 도전해요.",duration)
        elif t.distance(shark6)<15:
            exit(0)
        elif parts_map.isvisible() and t.distance(parts_map)<15:
            parts.color("pink")
            t.ontimer(self.parts_map_effect_done,100)
        else:
            t.ontimer(g.play,100)


    def result(self,msg,dur):
        if dur == 1:
            t.forward(15)
            t.write(msg,False,"center",("",20))
        else:
            t.goto(0,0)
            t.write(msg,False,"center",("",20))
            shark1.goto(r.randint(-1000,1000),r.randint(-650,650))
            shark2.goto(r.randint(-1000,1000),r.randint(-650,650))
            shark3.goto(r.randint(-1000,1000),r.randint(-650,650))
            shark4.goto(r.randint(-1000,1000),r.randint(-650,650))
            shark5.goto(r.randint(-1000,1000),r.randint(-650,650))
            parts.goto(r.randint(-1000,1000),r.randint(-650,650)) 
            rock1.goto(r.randint(-1000,1000),r.randint(-650,650))
            rock2.goto(r.randint(-1000,1000),r.randint(-650,650))
            rock3.goto(r.randint(-1000,1000),r.randint(-650,650))
            rock4.goto(r.randint(-1000,1000),r.randint(-650,650))
            parts_map.st()
            parts_map.goto(r.randint(-1000,1000),r.randint(-650,650))


g=Game()


t.setup(2560,1440)
t.bgcolor("skyblue")
t.shape("turtle")
t.speed(0)
t.penup()
t.goto(0,0)
t.color("white")
t.onkeypress(g.turn_right,"Right")
t.onkeypress(g.turn_up,"Up")
t.onkeypress(g.turn_left,"Left")
t.onkeypress(g.turn_down,"Down")
t.onkeypress(g.play,"space")
t.listen()

t.done()