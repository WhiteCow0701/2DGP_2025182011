import math
import os
from pico2d import *

open_canvas()

character = load_image(os.path.join(os.path.dirname(__file__), 'character.png'))
running = True

"""
def move_circle():
    print('CIRCLE')
    
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_character(x, y)    
    pass
"""

def move_top():
    print('TOP')
    for x in range(50, 750, 5):
        if not draw_character(x, 550):
            return

def draw_character(x, y):
    global running
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    delay(0.05)
    return running


def move_right():
    print('RIGHT')
    for y in range(550, 50, -5):
        if not draw_character(750, y):
            return
    pass

def move_bottom():
    print('BOTTOM')
    for x in range(750, 50, -5):
        if not draw_character(x, 50):
            return
    pass

def move_left():
    print('LEFT')
    for y in range(50, 550, 5):
        if not draw_character(50, y):
            return
    pass

def move_rectangle():
    print('RECTANGLE')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass
    
def move_triangle():
    print('TRIANGLE')
    pass


while True:
    #move_circle()
    move_rectangle()
    move_triangle()
    break

close_canvas()

