import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

TITLE = "Connect the sticks from 1 - 8"
nextsatellite = 0
satellites = []
number = 8
def create_satellites():
    for i in range(0, number):
        stick = Actor("stick")
        stick.pos = randint(40, WIDTH -40), randint(40, HEIGHT-40)
        satellites.append(stick)
def draw():
    screen.blit("space", (0,0))
    num = 1
    for i in satellites:
        screen.draw.text(str(num), (i.pos[0], i.pos[1] + 20))
        i.draw()
        num += 1
def update():
    pass

def on_mouse_down(pos):
    global nextsatellite
create_satellites()

pgzrun.go()