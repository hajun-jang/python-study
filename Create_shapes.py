import turtle as t

n=int(input("변의 수를 입력해 주세요:"))


t.pensize(3)
t.color("green")
t.fillcolor("yellow")


t.begin_fill()


for i in range(n):
    t.forward(1000/n)
    t.left(360/n)


t.end_fill()
t.done()