import pgzrun
from pgzero.builtins import *


from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

greet = Actor("greet")
greet.pos = 200, 200

def draw():
    screen.fill("green")
    greet.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_greet():
    greet.x = randint(20, (WIDTH - 20))
    greet.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def on_mouse_down():
  global score
  global greetclicked
  greetclicked = greet.collidepoint(greet.pos)
  if greet.collidepoint(greet.pos):
    score = score + 1
    place_greet()

clock.schedule(time_up, 10.0)
place_greet()




pgzrun.go()
screen = []