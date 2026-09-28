import math
import os
from pico2d import *

open_canvas()

character = load_image('character.png')
running = True


def move_circle():
    print('CIRCLE')
    
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        if not draw_character(x, y):
            return
    pass


def move_top():
    print('TOP')
    for x in range(50, 750, 5):
        if not draw_character(x, 550):
            return
    pass
           

def draw_character(x, y):
    global running
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False

    if not running:
        return False

    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)
    return True


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

def move_dot_to_dot(start, end):
    print('MOVE DOT TO DOT')
    x0, y0 = start
    x1, y1 = end
    n = 100
    

    for step in range(n + 1):
        t = step / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        if not draw_character(x, y):
            return
    
def move_triangle():
    print('TRIANGLE')
    A = (100, 100)
    B = (700, 100)
    C = (400, 500)

    move_dot_to_dot(A, B)
    move_dot_to_dot(B, C)
    move_dot_to_dot(C, A)
    
    


while True:
    if not running:
        break
    move_circle()
    if not running:
        break
    move_rectangle()
    if not running:
        break
    move_triangle()

close_canvas()


