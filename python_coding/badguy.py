import pygame, sys, random, time, math
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Space Invaders")
screen = pygame.display.set_mode((640, 650))
badguy_image = pygame.image.load("python_coding/images/badguy.png").convert()
badguy_image.set_colorkey((0,0,0))
last_badguy_spawn_time = 0
fighter_image = pygame.image.load("python_coding/images/fighter.png").convert()
fighter_image.set_colorkey((255,255,255))
missile_image = pygame.image.load("python_coding/images/missile.png").convert()
missile_image.set_colorkey((255,255,255))
font = pygame.font.Font(None,20)
GAME_OVER = pygame.image.load("python_coding/images/gameover.png").convert()
score = 0
shots = 0
hits = 0
misses = 0

class Badguy:
    def __init__(self):
        self.x = random.randint(0, 570)
        self.y = -100
        d=(math.pi/2)*random.random()-(math.pi/4)
        speed = random.randint(2, 6)
        self.dy = math.cos(d)*speed
        self.dx = math.sin(d)*speed

    def move(self):
        self.x += self.dx
        self.dy += 0.1
        self.y += self.dy

    def draw(self):
        screen.blit(badguy_image,(self.x,self.y))

    def bounce(self):
        if self.x < 0 or self.x > 570:
            self.dx *= -1

    def off_screen(self):
        return self.y > 640

    def touching(self,missile):
        return (self.x+35-missile.x)**2+(self.y+22-missile.y)**2 < 1225

    def score(self):
        global score
        score += 100

class Fighter:
    def __init__(self):
        self.x = 320
    def move(self):
        if pressed_keys[K_LEFT] and self.x > 0:
            self.x -= 3
        if pressed_keys[K_RIGHT] and self.x < 540:
            self.x += 3
    def draw(self):
        screen.blit(fighter_image,(self.x,591))
    def fire(self):
        global shots
        shots += 1
        missiles.append(Missile(self.x+50))
    def hit_by(self,badguy):
        return (
            badguy.y > 585 and
            badguy.x > self.x - 55 and
            badguy.x < self.x + 85
        )

class Missile:
    def __init__(self,x):
        self.x = x
        self.y = 591
    def move(self):
        self.y -= 5
    def off_screen(self):
        return self.y < -8
    def draw(self):
        screen.blit(missile_image,(self.x-4 ,self.y))

fighter = Fighter()
badguys = []
missiles = []

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            fighter.fire()
    pressed_keys = pygame.key.get_pressed()
    if time.time() - last_badguy_spawn_time > 0.5:
        badguys.append(Badguy())
        last_badguy_spawn_time = time.time()
    screen.fill((0,0,0))
    fighter.move()
    fighter.draw()
    i = 0
    while i < len(badguys):
        badguys[i].move()
        badguys[i].bounce()
        badguys[i].draw()
        if badguys[i].off_screen():
            del badguys[i]
            i -= 1
        i += 1
    i = 0
    while i < len(missiles):
        missiles[i].move()
        missiles[i].draw()
        if missiles[i].off_screen():
            del missiles[i]
            misses += 1
            i -= 1
        i += 1
    i = 0
    while i < len(badguys):
        j = 0
        while j < len(missiles):
            if badguys[i].touching(missiles[j]):
                badguys[i].score()
                hits += 1
                del badguys[i]
                del missiles[j]
                i -= 1
                break
            j += 1
        i += 1
    screen.blit(font.render("Score : "+str(score),True,(255,255,255)),(5,5))

    for badguy in badguys:
        if fighter.hit_by(badguy):
            screen.blit(GAME_OVER,(170,200))
            screen.blit(font.render(str(shots),True,(255,255,255)),(266,320))
            screen.blit(font.render(str(score),True,(255,255,255)),(266,348))
            screen.blit(font.render(str(hits),True,(255,255,255)),(400,320))
            screen.blit(font.render(str(misses),True,(255,255,255)),(400,337))
            if shots == 0:
                screen.blit(font.render("--",True,(255,255,255)),(400,357))
            else:
                screen.blit(font.render("{:.1f}%".format(100*hits/shots),True,(255,255,255)),(400,357))
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        sys.exit()
                pygame.display.update()

    pygame.display.update()