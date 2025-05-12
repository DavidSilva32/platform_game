from pgzero.actor import Actor
from settings import GRAVITY, GROUND_Y_CHARACTER, ENEMY_SPEED

class Enemy:
    def __init__(self, x, y, width):
        self.actor = Actor("enemy/enemy_idle", (x, y))
        self.velocity_y = 0
        self.on_ground = True
        self.speed = ENEMY_SPEED
        self.width_limit = width
        self.direction = 1
        self.facing_right = True

        # Animation
        self.run_frames = ["enemy/enemy_run1", "enemy/enemy_run2", "enemy/enemy_run3"]
        self.current_frame = 0
        self.frame_counter = 0

    def apply_gravity(self):
        self.velocity_y += GRAVITY
        self.actor.y += self.velocity_y

        if self.actor.y >= GROUND_Y_CHARACTER:
            self.actor.y = GROUND_Y_CHARACTER
            self.velocity_y = 0
            self.on_ground = True

    def move(self):
        self.actor.x += self.speed * self.direction

        # Patrulha entre bordas
        if self.actor.x > self.width_limit or self.actor.x < 0:
            self.direction *= -1
            self.facing_right = self.direction == 1

    def update_animation(self):
        self.frame_counter += 1
        if self.frame_counter % 10 == 0:
            self.current_frame = (self.current_frame + 1) % len(self.run_frames)

        # Escolhe a imagem baseada na direção
        base_image = self.run_frames[self.current_frame]
        if self.facing_right:
            self.actor.image = base_image
        else:
            self.actor.image = base_image + "_left"


    def update(self):
        self.apply_gravity()
        self.move()
        self.update_animation()

    def draw(self):
        self.actor.draw()
