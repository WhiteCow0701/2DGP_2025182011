import math
import os
from pico2d import *


open_canvas(800, 600)

character = load_image(os.path.join(os.path.dirname(__file__), 'character.png'))
running = True


def handle_events():
	global running

	for event in get_events():
		if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
			running = False


def draw_character(x, y):
	handle_events()
	if not running:
		return False

	clear_canvas()
	character.draw(x, y)
	update_canvas()
	delay(0.02)
	return True


def run_circle():
	center_x, center_y = 400, 300
	radius = 200

	for degree in range(360):
		theta = math.radians(degree)
		x = center_x + radius * math.cos(theta)
		y = center_y + radius * math.sin(theta)
		if not draw_character(x, y):
			return
