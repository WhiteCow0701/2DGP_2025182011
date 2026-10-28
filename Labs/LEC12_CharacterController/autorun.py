class AutoRun:
    DURATION = 5.0
    SPEED = 8
    DRAW_SIZE = 140
    MIN_X = 70
    MAX_X = 730

    def __init__(self):
        self.elapsed = 0.0

    def update(self, boy, delta_time):
        self.elapsed += delta_time
        boy.frame = (boy.frame + 1) % 8
        boy.x += boy.direction * self.SPEED

        if boy.x <= self.MIN_X or boy.x >= self.MAX_X:
            boy.x = max(self.MIN_X, min(boy.x, self.MAX_X))
            boy.direction *= -1

        return self.elapsed >= self.DURATION

    def draw(self, boy):
        boy.image.clip_composite_draw(
            boy.frame * 100, 0, 100, 100,
            0, 'h' if boy.direction == 1 else '',
            boy.x, boy.y, self.DRAW_SIZE, self.DRAW_SIZE
        )
