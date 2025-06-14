import pygame, sys, math, random, time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Pong")
screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()
ball_image = pygame.image.load("python_coding/images/ball.png").convert_alpha()
rscore = 0
lscore = 0
p = math.pi
match_start = time.time()
font = pygame.font.Font(None,40)
font2 = pygame.font.SysFont("corbel",70)
font3 = pygame.font.Font(None,60)
font4 = pygame.font.Font(None,30)

class Bat:
    def __init__(self,ctrls,x,side):
        self.ctrls = ctrls
        self.x = x
        self.y = 260
        self.side = side
        self.lastbop = 0

    def move(self):
        if pressed_keys[self.ctrls[0]] and self.y > 0:
            self.y -= 10
        if pressed_keys[self.ctrls[1]] and self.y < 520:
            self.y += 10

    def draw(self):
        offset = -self.side*(time.time() < self.lastbop+0.05)*10
        pygame.draw.line(screen,(255,255,255),(self.x,self.y),(self.x,self.y+80),6)

    def bop(self):
        if time.time() > self.lastbop + 0.3:
            self.lastbop = time.time()

class Ball:
    def __init__(self):
        self.d = (p/3)*random.random()+(p/3)+p*random.randint(0,1)
        self.speed = 12
        self.dx = math.sin(self.d)*self.speed
        self.dy = math.cos(self.d)*self.speed
        self.x = 475
        self.y = 275

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def draw(self):
        screen.blit(ball_image,(int(self.x),int(self.y)))

    def bounce(self):
        if (self.y <= 0 and self.dy < 0) or (self.y >= 550 and self.dy > 0):
            self.dy *= -1
            self.d = math.atan2(self.dx,self.dy)

        for bat in bats:
            if pygame.Rect(bat.x,bat.y,6,80).colliderect(self.x,self.y,50,50) and abs(self.dx)/self.dx == bat.side:
                self.d +=random.random()*p/4 - p/8
                if (0 < self.d < p/6) or (p*5/6 < self.d < p):
                    self.d = ((p/3)*random.random() + p/3)
                elif (p < self.d <p*7/6) or (p*11/6 < self.d < p*2):
                    self.d = ((p/3)*random.random()+(p/3))+p
                self.d *= -1
                self.d %= math.pi*2

                if time.time() < bat.lastbop + 0.05 and self.speed < 20:
                    self.speed *= 1.5
                self.dx = math.sin(self.d)*self.speed
                self.dy = math.cos(self.d)*self.speed

ball = Ball()
bats = [Bat([K_a,K_z,],10,-1),Bat([K_UP,K_DOWN],984,1)]

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                bats[0].bop()
            if event.key == K_LSHIFT:
                bats[1].bop()
    pressed_keys = pygame.key.get_pressed()

    screen.fill((0,0,0))

    pygame.draw.line(screen,(255,255,255),(screen.get_width()/2,0),(screen.get_width()/2,screen.get_height()),3)
    pygame.draw.circle(screen,(255,255,255),(int(screen.get_width()/2),int(screen.get_height()/2)),50,3)
    txt = font.render(str(int(60 - (time.time() - match_start))),True,(255,255,255))
    screen.blit(txt,(screen.get_width()/2 - txt.get_width()/2,20))

    for bat in bats:
        bat.move()
        bat.draw()

    if ball.x < -50:
        ball = Ball()
        rscore += 1

    if ball.x > 1000:
        ball = Ball()
        lscore += 1

    ball.move()
    ball.draw()
    ball.bounce()

    txt = font.render(str(lscore),True,(255,255,255))
    screen.blit(txt,(20,20))
    txt = font.render(str(rscore),True,(255,255,255))
    screen.blit(txt,(980-txt.get_width(),20))

    if time.time() - match_start > 60:
        txt = font2.render("score",True,(255,0,255))
        screen.blit(txt,(screen.get_width()/4 - txt.get_width()/2,screen.get_height()/4))
        screen.blit(txt,(screen.get_width()*3/4 - txt.get_width()/2,screen.get_height()/4))
        txt = font3.render(str(lscore),True,(255,255,255))
        screen.blit(txt,(screen.get_width()/4 - txt.get_width()/2,screen.get_height()/2))
        txt = font3.render(str(rscore),True,(255,255,255))
        screen.blit(txt,(screen.get_width()*3/4 - txt.get_width()/2,screen.get_height()/2))
        txt = font4.render("Press Spsce to restart",True,(255,255,255))
        screen.blit(txt,(screen.get_width()*5/9,screen.get_height()-50))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_SPACE]:
                    lscore = 0
                    rscore = 0
                    bats[0].y = 200
                    bats[1].y = 200
                    exit = True
                    match_start = time.time()
                    ball = Ball()
                    break
            if exit:
                exit = False
                break
            pygame.display.update()

    pygame.display.update()