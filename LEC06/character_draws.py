import math
from pico2d import *

open_canvas()

character = load_image('character.png')

def move_circle():
    print('CIRCLE')
    
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        clear_canvas()
        character.draw(x,y)
        update_canvas()
        delay(0.05)
    pass

def move_top():
    print('TOP')

def move_right():
    print('RIGHT')

def move_bottom():
    print('BOTTOM')

def move_left():
    print('LEFT')

   
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
    move_circle()
    move_rectangle()
    move_triangle()
    break


