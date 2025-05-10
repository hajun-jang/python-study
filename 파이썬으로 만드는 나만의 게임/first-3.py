'''오늘 할 것:
    2.3:제어문:
        2.3.1:조건문
        2.3.2:반복문
    2.4:함수:
        2.4.1:반환 없는 함수
        2.4.2:반환 있는 함수
        2.4.3:전역변수와 지역변수
    2.5:객체와 클래스
    2.6:모듈:
        2.6.1:시간 모듈
        2.6.2:랜덤 모듈'''
#2.3.1
fire = True
if fire:    #조건문
    print("미사일 발사!")
print("-"*100)  #칸 나누기
key = "RIGHT"
if key == "LEFT":   #조건문 1
    print("왼쪽으로 이동")
elif key == "RIGHT":    #조건문 2
    print("오른쪽으로 이동")
else:
    print("정지")
print("-"*100)  #칸 나누기
###################################################
#2.3.2
i = 0
while i < 3:
    print("미사일 발사!")
    i = i + 1
print("-"*100)  #칸 나누기
i = 0
for i in range(0, 3):
    print(i)
    print("적 등장!")
print("-"*100)  #칸 나누기
enemy = ["적1","적2","적3"]
for e in enemy:
    print(e)
print("-"*100)  #칸 나누기
###################################################
#2.4.1
def fire():
    print("미사일 발사!")

fire()
fire()
fire()
print("-"*100)  #칸 나누기
def fire(n=3):  #반환값이 있음. 만약 없으면,기본값을 3으로 설정.
    for i in range(0, n):
        print("미사일 발사!")

fire()
fire(2)
print("-"*100)  #칸 나누기
def fire(kind, n):
    for i in range(0, n):
        if kind =='machine_gun':
            print("기관총 발사!")
        elif kind =='missile':
            print("미사일 발사!")
        elif kind == 'bomb':
            print("폭탄 발사!")
        else:
            print("무기 없음")
fire('machine_gun',3)
fire('missile',2)
fire('bomb',1)
print("-"*100)  #칸 나누기
###################################################
#2.4.2
def add(n1, n2):
    return n1 + n2
r = add(3, 5)
print(r)
print(add(4, 7))
print("-"*100)  #칸 나누기
def sum(*li):
    sum = 0
    for i in li:
        sum += i
    return sum
print(sum(1, 2, 3, 4, 5))
print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print("-"*100)  #칸 나누기
def sum_avg(*li):
    sum = 0
    for i in li:
        sum += i
    return sum, sum/len(li)
print(sum_avg(1, 2, 3, 4, 5))
print(sum_avg(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print("-"*100)  #칸 나누기
###################################################
#2.4.3
s = 'Suan'
print(s)
def string_plus(s1, s2):
    s = s1 + s2
    return s
print(s)
s = string_plus('Suan', 'Lab')
print(s)
def gloabl_plus(s1, s2):
    gs = s + s1 + s2
    return gs
print(s)
s = gloabl_plus('Suan','Lab')
print(s)
print("-"*100)  #칸 나누기
###################################################
#2.5
class Fighter(object):
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile
    def atttack(self):
        print(self.model + "출격!")
    def fire(self):
        print(self.missile + "발사!")
fighter = Fighter("F-22","공대공미사일")
fighter.atttack()
fighter.fire()
print("-"*100)  #칸 나누기
###################################################
#2.6.1
import time
print(time.time())
print("-"*100)  #칸 나누기
#여기에선 모듈을 다시 불러오지 않습니다.
now = time.localtime(time.time())
print(now)
year = str(now.tm_year)
month = str(now.tm_mon)
day = str(now.tm_mday)
print(year + "년" + month + "월" + day + "일")
hour = str(now.tm_hour)
minute = str(now.tm_min)
sec = str(now.tm_sec)
print(hour + "시" + minute + "분" + sec + "초")
print("-"*100)  #칸 나누기
###################################################
#2.6.2
import random
print(random.random())
print(random.randint(1, 10))
print(random.randrange(0, 10, 2))
print("-"*100)  #칸 나누기
li = [10, 20, 30, 40, 50]
print(li)
print(random.choice(li))
print(random.sample(li, 2))
random.shuffle(li)
print(li)
#done#
