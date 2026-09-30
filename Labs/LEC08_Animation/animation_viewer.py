from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_WIDTH = 200
FRAME_HEIGHT = 200
DRAW_WIDTH = 360
DRAW_HEIGHT = 360
ANIMATION_REPEAT_LIMIT = 5
PAUSE_SECONDS = 1.0


# 추가 점수: 애니메이션마다 프레임 수와 프레임 크기, 출력 크기를 다르게 설정할 수 있다.
def make_animation(
    name,
    row,
    frame_count=4,
    frame_delay=0.12,
    frame_width=FRAME_WIDTH,
    frame_height=FRAME_HEIGHT,
    draw_size=(DRAW_WIDTH, DRAW_HEIGHT),
):
    return {
        'name': name,
        'frames': [
            (frame * frame_width, row * frame_height, frame_width, frame_height)
            for frame in range(frame_count)
        ],
        'draw_size': draw_size,
        'frame_delay': frame_delay,
    }


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    sprite_sheet = load_image('sprite_sheet_hw.png')
    grass = load_image('grass.png')

    animations = [
        # 추가 점수 예시: 점프는 3프레임, 공격은 별도 출력 크기를 사용한다.
        make_animation('walk', 3),
        make_animation('run', 2),
        make_animation('jump', 1, frame_count=3),
        make_animation('attack', 0, draw_size=(320, 320)),
    ]

    animation_index = 0
    frame_index = 0
    repeat_count = 0
    last_frame_time = get_time()
    pause_until = 0.0
    running = True

    while running:
        for event in get_events():
            if event.type == SDL_QUIT:
                running = False

        current_time = get_time()
        animation = animations[animation_index]

        if pause_until and current_time >= pause_until:
            animation_index = (animation_index + 1) % len(animations)
            frame_index = 0
            repeat_count = 0
            pause_until = 0.0
            last_frame_time = current_time
            animation = animations[animation_index]

        if not pause_until and current_time - last_frame_time >= animation['frame_delay']:
            last_frame_time = current_time
            if frame_index == len(animation['frames']) - 1:
                repeat_count += 1
                if repeat_count >= ANIMATION_REPEAT_LIMIT:
                    pause_until = current_time + PAUSE_SECONDS
                else:
                    frame_index = 0
            else:
                frame_index += 1

        clear_canvas()
        grass.draw(CANVAS_WIDTH // 2, 30)

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

        update_canvas()
        delay(0.01)

    close_canvas()


if __name__ == '__main__':
    main()