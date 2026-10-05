import os

from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525
DRAW_SIZE = 220
FRAME_INTERVAL = 0.1
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0
SPRITE_FILENAME = 'sonic-sprite.png'
SPRITE_PATH = os.path.join(os.path.dirname(__file__), SPRITE_FILENAME)


def make_row(
	name,
	frame_count,
	bottom,
	frame_width=40,
	frame_height=50,
	frame_interval=FRAME_INTERVAL,
):
	frames = [
		(
			index * frame_width,
			bottom,
			min(frame_width, SPRITE_WIDTH - index * frame_width),
			frame_height,
		)
		for index in range(frame_count)
	]
	return {
		'name': name,
		'frames': frames,
		'frame_interval': frame_interval,
		'draw_size': (DRAW_SIZE, DRAW_SIZE),
	}


def build_animations():
	return [
		make_row('walk', 10, 405, frame_interval=0.1),
		make_row('run', 10, 350, frame_interval=0.09),
		make_row('jump', 8, 295, frame_interval=0.12),
		make_row('spin', 8, 235, frame_interval=0.1),
		make_row('attack', 6, 180, frame_interval=0.11),
		make_row('fall', 6, 125, frame_interval=0.12),
		make_row('celebrate', 8, 70, frame_height=45, frame_interval=0.12),
		make_row('pose', 8, 15, frame_height=40, frame_interval=0.12),
	]


def validate_animations(animations):
	for animation in animations:
		if not animation['frames']:
			raise ValueError('애니메이션 프레임이 비어 있습니다.')
		if animation['frame_interval'] <= 0:
			raise ValueError('프레임 간격은 0보다 커야 합니다.')
		for left, bottom, width, height in animation['frames']:
			if left < 0 or bottom < 0:
				raise ValueError('프레임 좌표는 음수일 수 없습니다.')
			if left + width > SPRITE_WIDTH or bottom + height > SPRITE_HEIGHT:
				raise ValueError('스프라이트 시트 영역을 벗어난 프레임입니다.')


def draw_frame(sprite_sheet, animation, frame_index):
	left, bottom, width, height = animation['frames'][frame_index]
	draw_width, draw_height = animation['draw_size']
	sprite_sheet.clip_draw(
		left,
		bottom,
		width,
		height,
		CANVAS_WIDTH // 2,
		CANVAS_HEIGHT // 2,
		draw_width,
		draw_height,
	)


def handle_events():
	for event in get_events():
		if event.type == SDL_QUIT:
			return False
		if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
			return False
	return True
