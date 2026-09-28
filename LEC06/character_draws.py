import math

def move_circle():
    print('circle')
    
def move_rectangle():
    print('rectangle')
    
def move_triangle():
    print('triangle')
    
while True:
    move_circle()
    move_rectangle()
    move_triangle()
    break

from pico2d import *

open_canvas(800, 600)
boy = load_image('character.png')

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)
close_canvas()

theta = math.radians(degree)
x = 400 + 200 * math.cos(theta)
y = 300 + 200 * math.sin(theta)