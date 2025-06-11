# 256 페이지부터 시작!
import pygame, sys, time, random, math
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("fly Cather")
screen = pygame.display.set_mode((1000,600))
fly_image = pygame.image.load("python_coding/images/fly.png").convert_alpha()
fly_sound = pygame.mixer.Sound("python_coding/sounds/fly-buzz.ogg")
homescreen_image = pygame.image.load("python_coding/images/flycatcher_home.png").convert_alpha()
frog_image = pygame.image.load("python_coding/images/frog.png").convert_alpha()
tounge_sound = pygame.mixer.Sound("python_coding/sounds/tongue.ogg")
font = pygame.font.SysFont("draglinebtndm",60)
menu = "start"

class Fly:
    def __init__(self):
        self.x = random.randint(0,screen.get_width()-fly_image.get_width())
        self.y = random.randint(0,screen.get_height()-fly_image.get_height())
        self.dir = random.randint(0,359)
        self.spawn_time = time.time()
        fly_sound.play()
        self.stuck = False

    def draw(self):
        if self.stuck:
            tpos = frog.get_tongue_pos()
            screen.blit(fly_image,(tpos[0]-fly_image.get_width()/2,tpos[1]-fly_image.get_height()/2))
        elif time.time() > self.spawn_time+1.4 and time.time() < self.spawn_time+3.4:
            rotated = pygame.transform.rotate(fly_image,self.dir)
            screen.blit(rotated,(self.x,self.y))

    def stick(self):
        if not self.stuck and time.time() > self.spawn_time + 1.4 and time.time() < self.spawn_time + 3.4:
            tpos = frog.get_tongue_pos()
            fpos = (self.x+fly_image.get_width()/2,self.y+fly_image.get_height()/2)
            if (tpos[0]-fpos[0])**2+(tpos[1]-fpos[1])**2 < (fly_image.get_width()/2+10)**2:
                self.stuck = True

class Frog:
    def __init__(self):
        self.dir = 0
        self.tongue_dist = 0
        self.tongue_extend = 0

    def move(self):
        self.tongue_dist += self.tongue_extend * 10
        if self.tongue_dist**2 > (fly.x-screen.get_width()/2)**2 + (fly.y-screen.get_height()/2)**2:
            self.tongue_extend = -1
        if self.tongue_dist == 0:
            self.tongue_extend = 0
            if pressed_keys[K_LEFT]:
                self.dir += 4
            if pressed_keys[K_RIGHT]:
                self.dir -= 4

    def draw(self):
        tpos = self.get_tongue_pos()
        pygame.draw.circle(screen,(255,50,50),tpos,10)
        pygame.draw.line(screen,(255,50,50),(screen.get_width()/2,screen.get_height()/2),tpos,10)
        rotated = pygame.transform.rotate(frog_image,self.dir)
        screen.blit(rotated,(screen.get_width()/2-rotated.get_width()/2,screen.get_height()/2-rotated.get_height()/2))

    def get_tongue_pos(self):
        return (
            int(screen.get_width()/2-self.tongue_dist*math.sin(math.radians(self.dir))),
            int(screen.get_height()/2-self.tongue_dist*math.cos(math.radians(self.dir)))
        )
    
    def tongue_poke(self):
        if self.tongue_dist == 0:
            self.tongue_extend = 5
            tounge_sound.play()

fly = None
frog = Frog()

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE:
            frog.tongue_poke()
    pressed_keys = pygame.key.get_pressed()

    if menu == "start":
        screen.blit(homescreen_image,(0,0))
        txt = font.render("Play",True,(255,255,255))
        txt_x = 705
        txt_y = 435
        buttonrect = pygame.Rect((txt_x,txt_y),txt.get_size())
        pygame.draw.rect(screen,(200,50,0),buttonrect)
        screen.blit(txt, (txt_x, txt_y))
    if pygame.mouse.get_pressed()[0] and buttonrect.collidepoint(pygame.mouse.get_pos()):
        menu = "game"

    if menu == "game":
        if fly == None or (time.time() > fly.spawn_time + 4.4 and not fly.stuck):
            fly = Fly()
        if fly.stuck and frog.tongue_dist == 0:
            fly = Fly()
        screen.fill((255,255,255))
        frog.move()
        frog.draw()
        fly.stick()
        fly.draw()
    pygame.display.update()