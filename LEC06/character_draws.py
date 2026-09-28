import math
import os
from pico2d import *

open_canvas()

character = load_image(os.path.join(os.path.dirname(__file__), 'character.png'))

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
        draw_character(x, 550)
    pass
           

def draw_character(x, y):
    global running
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.05)


def move_right():
    print('RIGHT')
    for y in range(550, 50, -5):
        draw_character(750, y)
    pass

def move_bottom():
    print('BOTTOM')
    for x in range(750, 50, -5):
        draw_character(x, 50)
    pass

def move_left():
    print('LEFT')
    for y in range(50, 550, 5):
        draw_character(50, y)
    pass
"""
def move_rectangle():
    print('RECTANGLE')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass
"""
def move_dot_to_dot(start, end):
    print('MOVE DOT TO DOT')
    x0, y0 = start
    x1, y1 = end
    n = 100
    

    for step in range(n + 1):
        t = step / n
        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t
        draw_character(x, y)
    
def move_triangle():
    print('TRIANGLE')
    A = (100, 100)
    B = (700, 100)
    C = (400, 500)

    move_dot_to_dot(C, A)
    
    


while True:
    #move_circle()
    #move_rectangle()
    move_triangle()
    break

close_canvas()

