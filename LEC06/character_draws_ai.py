from pico2d import *
import math

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('character.png')


DELAY = 0.015     # 이동 속도 딜레이
running = True


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def render(x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.draw(x, y)
    update_canvas()
    handle_events()   # OS 이벤트를 주기적으로 처리하여 '응답 없음' 방지
    delay(DELAY)
    return running


def run_circle():
    cx, cy = 400, 300
    r = 210

    # (400, 90) 위치인 -90도부터 시작하여 한 바퀴(360도) 회전
    for degree in range(-90, 270, 2):
        rad = math.radians(degree)
        x = cx + r * math.cos(rad)
        y = cy + r * math.sin(rad)
        if not render(x, y):
            return


def run_rectangle():
    # 1. 하단 중앙 -> 우하단
    for x in range(400, 750 + 1, 4):
        if not render(x, 90): return

    # 2. 우하단 -> 우상단
    for y in range(90, 550 + 1, 4):
        if not render(750, y): return

    # 3. 우상단 -> 좌상단
    for x in range(750, 50 - 1, -4):
        if not render(x, 550): return

    # 4. 좌상단 -> 좌하단
    for y in range(550, 90 - 1, -4):
        if not render(50, y): return

    # 5. 좌하단 -> 하단 중앙
    for x in range(50, 400 + 1, 4):
        if not render(x, 90): return


def run_triangle():
    # 1. 하단 중앙 -> 우하단
    for x in range(400, 750 + 1, 4):
        if not render(x, 90): return

    # 2. 우하단 -> 상단 꼭짓점
    steps = 150
    for i in range(steps + 1):
        t = i / steps
        x = 750 + (400 - 750) * t
        y = 90 + (550 - 90) * t
        if not render(x, y): return

    # 3. 상단 꼭짓점 -> 좌하단
    for i in range(steps + 1):
        t = i / steps
        x = 400 + (50 - 400) * t
        y = 550 + (90 - 550) * t
        if not render(x, y): return

    # 4. 좌하단 -> 하단 중앙
    for x in range(50, 400 + 1, 4):
        if not render(x, 90): return


# 각 운동을 한 번씩 순차적으로 수행하며 무한 반복
# 원운동 (1회) -> 사각 운동 (1회) -> 삼각 운동 (1회) -> 다시 반복
while running:
    run_circle()
    run_rectangle()
    run_triangle()

close_canvas()
