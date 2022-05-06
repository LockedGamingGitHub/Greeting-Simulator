import pgzrun
from pgzero.builtins import *


WIDTH = 800
HEIGHT = 600
TITLE = "Greeting Simulator 2.0 BETA"

player = Actor("player")
player.pos = 100, 100

def draw():
    screen.clear()
    screen.fill("green")
    player.draw()
def update():
    if keyboard.left:
      player.x = player.x - 2
    elif keyboard.right:
      player.x = player.x + 2
    elif keyboard.up:
        player.y = player.y - 2
    elif keyboard.down:
        player.y = player.y + 2


pgzrun.go()
screen = []