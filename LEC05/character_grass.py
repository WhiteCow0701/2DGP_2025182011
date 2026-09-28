from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

cx, cy = 400, 300  
r = 200           
angle = 0           

while True:
    clear_canvas()
    x = cx + r * math.cos(angle)
    y = cy + r * math.sin(angle)
    character.draw(int(x), int(y))
    update_canvas()
    angle += 0.03   
    delay(0.01)

close_canvas()
