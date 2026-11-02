from pico2d import get_canvas_width, load_image


class Ball:
    SPEED = 10
    HALF_SIZE = 10

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = load_image('ball21x21.png')
        self.is_out_of_bounds = False

    def update(self):
        self.x += self.direction * self.SPEED
        self.is_out_of_bounds = (
            self.x < -self.HALF_SIZE or
            self.x > get_canvas_width() + self.HALF_SIZE
        )

    def draw(self):
        self.image.draw(self.x, self.y)
