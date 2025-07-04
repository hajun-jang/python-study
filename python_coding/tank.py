import pygame, sys, math, random, time
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Tank battle")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,600))
homescreen_image = pygame.image.load("python_coding/images/TBhomescreen.jpg").convert()
landscape_image = pygame.image.load("python_coding/images/landscape.jpg").convert()
wall_image = pygame.image.load("python_coding/images/wall.png").convert()
vert_wall_image = pygame.transform.rotate(wall_image,90)
tankG_image = pygame.image.load("python_coding/images/tankG.png").convert_alpha()
tankB_image = pygame.image.load("python_coding/images/tankB.png").convert_alpha()
shell_sound = pygame.mixer.Sound("python_coding/sounds/shell.ogg")
harm_sound = pygame.mixer.Sound("python_coding/sounds/tank_hit.ogg")
pygame.mixer.init(buffer=512)
menu = "home"

class Wall:
    def __init__(self,x,y,vert):
        self.x = x
        self.y = y
        self.vert = vert
        self.speed = 1

    def draw(self):
        if self.vert:
            screen.blit(vert_wall_image,(self.x,self.y))
        else:
            screen.blit(wall_image,(self.x,self.y))

    def move(self):
        if self.vert:
            self.y += self.speed
        else:
            self.x += self.speed
        if (
            (self.vert and (self.y < 50 or self.y > 350)) or 
            (not self.vert and ((self.x < 50 or self.x > 750) or 
            (self.x > 200 and self.x < 600)))):
            self.speed *= -1

class Tank:
    def __init__(self,x,y,dir,ctrls,img):
        self.x = x
        self.y = y
        self.ctrls = ctrls
        self.dir = dir
        self.img = img
        self.flash_time_end = 0
        self.lives = 3
    def draw(self):
        if time.time() > self.flash_time_end or time.time()%0.1 < 0.05:
            rotated = pygame.transform.rotate(self.img,self.dir)
            screen.blit(rotated,(self.x+self.img.get_width()/2-rotated.get_width()/2,self.y+self.img.get_height()/2-rotated.get_height()/2))
    def move(self):
        dx = math.sin(math.radians(self.dir))
        dy = math.cos(math.radians(self.dir))
        if pressed_keys[self.ctrls[0]]:
            self.x -= dx
            self.y -= dy
        if pressed_keys[self.ctrls[1]]:
            self.x += 0.5 * dx
            self.y += 0.5 * dy
        if pressed_keys[self.ctrls[2]]:
            self.dir += 1
        if pressed_keys[self.ctrls[3]]:
            self.dir -= 1
    def fire(self):
        shells.append(Shell(self.x+self.img.get_width()/2,self.y+self.img.get_height()/2,self.dir))
    def hit_shell(self,shell):
        return pygame.Rect(self.x,self.y+10,60,60).collidepoint(shell.x,shell.y)
    def harm(self):
        if time.time() > self.flash_time_end:
            self.flash_time_end = time.time() + 2
            self.lives -= 1

class Shell:
    def __init__(self,x,y,dir):
        self.dx = -math.sin(math.radians(dir))*5
        self.dy = -math.cos(math.radians(dir))*5
        self.x = x + self.dx * 8
        self.y = y + self.dy * 8
        self.bounces = 0
        shell_sound.play()
    def move(self):
        self.x += self.dx
        self.y += self.dy
    def draw(self):
        pygame.draw.circle(screen,(100,50,50),(int(self.x),int(self.y)),3)
    def bounce(self):
        for wall in walls:
            if wall.vert and pygame.Rect((wall.x,wall.y),vert_wall_image.get_size()).collidepoint(self.x,self.y):
                self.dx *= -1
                self.bounces += 1
            if not wall.vert and pygame.Rect((wall.x,wall.y),wall_image.get_size()).collidepoint(self.x,self.y):
                self.dy *= -1
                self.bounces += 1
            if self.x < 0 or self.x > 1000:
                self.dx *= -1
                self.bounces += 0.2
                time.sleep(0.01)
            if self.y < 0 or self.y > 600:
                self.dy *= -1
                self.bounces += 0.2
                time.sleep(0.01)

walls = [Wall(496,200,True),Wall(50,150,False),Wall(600,150,False),Wall(50,435,False),Wall(600,435,False)]
tankG = Tank(740,20,180,(K_UP,K_DOWN,K_LEFT,K_RIGHT),tankG_image)
tankB = Tank(200,500,0,(K_w,K_s,K_a,K_d),tankB_image)
shells = []
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RSHIFT and menu == "game":
            tankG.fire()
        if event.type == KEYDOWN and event.key == K_q and menu == "game":
            tankB.fire()
    
    pressed_keys = pygame.key.get_pressed()

    if menu == "home":
        screen.blit(homescreen_image,(0,0))
        buttonrect = pygame.Rect(409,440,147,147)
        if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
            menu = "game"

    if menu == "game":
        tankG.move()
        tankB.move()
        screen.blit(landscape_image,(0,0))
        tankG.draw()
        tankB.draw()
        for wall in walls:
            wall.move()
            wall.draw()
        
        i = 0
        while i < len(shells):
            shells[i].move()
            shells[i].bounce()
            shells[i].draw()
            flag = False

            if tankG.hit_shell(shells[i]):
                tankG.harm()
                harm_sound.play()
                flag = True
            if tankB.hit_shell(shells[i]):
                tankB.harm()
                harm_sound.play()
                flag = True
            if shells[i].bounces >= 5:
                flag = True

            if flag:
                del shells[i]
                i -= 1
            i += 1

    pygame.display.update()