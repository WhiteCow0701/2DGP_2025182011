import math

from pico2d import get_time, load_image
from transitions import Machine

from autorun import AutoRun


class Boy:
    IDLE_DURATION = 5.0
    MIN_X = 50
    MAX_X = 750

    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.direction = 1
        self.speed = 5
        self.image = load_image('animation_sheet.png')
        self.idle_timer = 0.0
        self._last_update_time = get_time()
        self.autorun = AutoRun()
        self.machine = Machine(
            model=self,
            states=['IDLE', 'RUN', 'SLEEP', 'AUTORUN'],
            initial='IDLE',
            auto_transitions=False,
        )
        self.machine.add_transition(
            trigger='sleep',
            source='IDLE',
            dest='SLEEP',
        )
        self.machine.add_transition(
            trigger='wake_up',
            source='SLEEP',
            dest='IDLE',
            after='reset_idle_timer',
        )
        self.machine.add_transition(
            trigger='start_running',
            source=['IDLE', 'SLEEP'],
            dest='RUN',
            after='reset_idle_timer',
        )
        self.machine.add_transition(
            trigger='stop_running',
            source='RUN',
            dest='IDLE',
            after='reset_idle_timer',
        )
        self.machine.add_transition(
            trigger='start_autorun',
            source='IDLE',
            dest='AUTORUN',
            after='reset_autorun',
        )
        self.machine.add_transition(
            trigger='finish_autorun',
            source='AUTORUN',
            dest='IDLE',
            after='reset_idle_timer',
        )
        self.machine.add_transition(
            trigger='cancel_autorun',
            source='AUTORUN',
            dest='RUN',
            after='reset_idle_timer',
        )
    
    def update(self):
        current_time = get_time()
        delta_time = current_time - self._last_update_time
        self.idle_timer += delta_time
        self._last_update_time = current_time

        if self.state == 'IDLE':
            self.frame = (self.frame + 1) % 8
            if self.idle_timer >= self.IDLE_DURATION:
                self.sleep()
        elif self.state == 'RUN':
            self.frame = (self.frame + 1) % 8
            self.x += self.direction * self.speed
            self.x = max(self.MIN_X, min(self.x, self.MAX_X))
        elif self.state == 'AUTORUN':
            if self.autorun.update(self, delta_time):
                self.finish_autorun()

    def draw(self):
        if self.state == 'IDLE':
            self.image.clip_draw(self.frame * 100, 300, 100, 100,
                                self.x, self.y )
        elif self.state == 'RUN':
            self.image.clip_composite_draw(
                self.frame * 100, 0, 100, 100,
                0, 'h' if self.direction == 1 else '',
                self.x, self.y, 100, 100
            )
        elif self.state == 'AUTORUN':
            self.autorun.draw(self)
        elif self.state == 'SLEEP':
            self.image.clip_composite_draw(
                0, 300, 100, 100,
                math.pi / 2, '', self.x, self.y - 30, 100, 100
            )

    def set_direction(self, direction):
        self.direction = direction

    def reset_idle_timer(self):
        self.idle_timer = 0.0
        self._last_update_time = get_time()

    def reset_autorun(self):
        self.autorun.elapsed = 0.0
        self._last_update_time = get_time()

    