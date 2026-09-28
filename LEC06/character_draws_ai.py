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
	print('CIRCLE')
	center_x, center_y = 400, 300
	radius = 200

	for degree in range(360):
		theta = math.radians(degree)
		x = center_x + radius * math.cos(theta)
		y = center_y + radius * math.sin(theta)
		if not draw_character(x, y):
			return


def run_rectangle():
	print('RECTANGLE')
	for x in range(100, 701, 4):
		if not draw_character(x, 100):
			return

	for y in range(100, 501, 4):
		if not draw_character(700, y):
			return

	for x in range(700, 99, -4):
		if not draw_character(x, 500):
			return

	for y in range(500, 99, -4):
		if not draw_character(100, y):
			return


def move_dot_to_dot(start, end):
	x0, y0 = start
	x1, y1 = end
	steps = max(abs(x1 - x0), abs(y1 - y0))

	for step in range(steps + 1):
		t = step / steps
		x = x0 + (x1 - x0) * t
		y = y0 + (y1 - y0) * t
		if not draw_character(x, y):
			return


def run_triangle():
	print('TRIANGLE')
	point_a = (100, 100)
	point_b = (700, 100)
	point_c = (400, 500)

	move_dot_to_dot(point_a, point_b)
	move_dot_to_dot(point_b, point_c)
	move_dot_to_dot(point_c, point_a)


while running:
	run_circle()
	if not running:
		break
	run_rectangle()
	if not running:
		break
	run_triangle()

close_canvas()
