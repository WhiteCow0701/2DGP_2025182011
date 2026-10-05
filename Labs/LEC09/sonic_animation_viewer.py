import os

from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 600
SPRITE_WIDTH = 399
SPRITE_HEIGHT = 525
DRAW_SIZE = 110
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
	frame_ranges=None,
):
	if frame_ranges is None:
		frame_ranges = [
			(index * frame_width, (index + 1) * frame_width)
			for index in range(frame_count)
		]
	frames = [
		(left, bottom, right - left, frame_height)
		for left, right in frame_ranges
	]
	return {
		'name': name,
		'frames': frames,
		'frame_interval': frame_interval,
		'draw_size': (DRAW_SIZE, DRAW_SIZE),
	}


def build_animations():
	return [
		make_row(
			'walk', 9, 447, frame_height=39, frame_interval=0.1,
			frame_ranges=[(0, 30), (30, 58), (58, 118), (118, 150), (150, 182),
				(182, 269), (269, 297), (297, 335), (335, 375)],
		),
		make_row(
			'run', 12, 408, frame_height=39, frame_interval=0.09,
			frame_ranges=[(0, 36), (36, 64), (64, 96), (96, 134), (134, 168),
				(168, 203), (203, 235), (235, 262), (262, 294), (294, 332),
				(332, 368), (368, 399)],
		),
		make_row(
			'jump', 6, 362, frame_height=43, frame_interval=0.12,
			frame_ranges=[(0, 37), (37, 81), (81, 126), (126, 172), (172, 221), (221, 261)],
		),
		make_row(
			'spin', 9, 326, frame_height=34, frame_interval=0.1,
			frame_ranges=[(0, 33), (33, 65), (65, 97), (97, 130), (130, 161),
				(161, 193), (193, 229), (229, 264), (264, 298)],
		),
		make_row(
			'spin_fast', 6, 293, frame_height=27, frame_interval=0.1,
			frame_ranges=[(0, 35), (35, 67), (67, 102), (102, 136), (136, 171), (171, 207)],
		),
		make_row(
			'spin_jump', 6, 252, frame_height=36, frame_interval=0.1,
			frame_ranges=[(0, 36), (36, 70), (70, 108), (108, 145), (145, 182), (182, 217)],
		),
		make_row(
			'attack', 6, 208, frame_height=35, frame_interval=0.11,
			frame_ranges=[(0, 33), (33, 69), (69, 116), (116, 167), (167, 215), (215, 256)],
		),
		make_row(
			'fall', 8, 155, frame_height=45, frame_interval=0.12,
			frame_ranges=[(0, 28), (28, 62), (62, 87), (87, 117), (117, 146),
				(146, 176), (176, 228), (228, 271)],
		),
		make_row(
			'celebrate', 8, 109, frame_height=39, frame_interval=0.12,
			frame_ranges=[(0, 29), (29, 63), (63, 96), (96, 134), (134, 172),
				(172, 212), (212, 252), (252, 287)],
		),
		make_row(
			'pose', 4, 57, frame_height=41, frame_interval=0.12,
			frame_ranges=[(0, 45), (45, 89), (89, 121), (121, 160)],
		),
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


def run_viewer():
	animations = build_animations()
	validate_animations(animations)

	open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
	sprite_sheet = load_image(SPRITE_PATH)

	animation_index = 0
	frame_index = 0
	repeat_count = 0
	frame_elapsed = 0.0
	pause_until = None
	previous_time = get_time()
	running = True

	while running:
		running = handle_events()
		current_time = get_time()
		elapsed = min(current_time - previous_time, 0.1)
		previous_time = current_time
		animation = animations[animation_index]

		if pause_until is None:
			frame_elapsed += elapsed
			while frame_elapsed >= animation['frame_interval']:
				frame_elapsed -= animation['frame_interval']
				frame_index += 1
				if frame_index >= len(animation['frames']):
					frame_index = 0
					repeat_count += 1
					if repeat_count >= REPEAT_COUNT:
						pause_until = current_time + PAUSE_SECONDS

		if pause_until is not None and current_time >= pause_until:
			animation_index = (animation_index + 1) % len(animations)
			frame_index = 0
			repeat_count = 0
			frame_elapsed = 0.0
			pause_until = None
			animation = animations[animation_index]

		clear_canvas()
		draw_frame(sprite_sheet, animation, frame_index)
		update_canvas()

	close_canvas()


if __name__ == '__main__':
	run_viewer()
