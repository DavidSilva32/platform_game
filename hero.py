from pgzero.actor import Actor
from pgzero.builtins import Rect
from pgzero.builtins import music
from settings import GRAVITY, GROUND_Y_CHARACTER, HERO_SPEED, JUMP_STRENGTH, HERO_HEALTH, HERO_INVULNERABLE_TIME

class Hero:
    def __init__(self, x, y, platforms=[]):
        self.actor = Actor("hero/hero_idle", (x, y))
        self.velocity_y = 0
        self.on_ground = False
        self.facing_right = True
        self.run_frames = ["hero/hero_run1", "hero/hero_run2", "hero/hero_run3"]
        self.current_frame = 0
        self.frame_counter = 0
        self.state = "idle"
        self.health = HERO_HEALTH
        self.invulnerable = False
        self.invulnerable_timer = 0
        self.visible = True
        self.platforms = platforms

    def move_left(self):
        self.actor.x -= HERO_SPEED
        self.facing_right = False
        self.state = "run"

    def move_right(self):
        self.actor.x += HERO_SPEED
        self.facing_right = True
        self.state = "run"

    def jump(self):
        if self.on_ground:
            self.velocity_y = -JUMP_STRENGTH
            self.on_ground = False
            self.state = "jump"

    def apply_gravity(self):
        self.velocity_y += GRAVITY
        self.actor.y += self.velocity_y

    def check_platform_collision(self):
        future_rect = Rect(
            (self.actor.x - self.actor.width // 2, self.actor.y - self.actor.height // 2),
            (self.actor.width, self.actor.height)
        )
        landed = False

        for platform in self.platforms:
            platform_rect = platform['rect']

            if future_rect.colliderect(platform_rect) and self.velocity_y >= 0:
                self.actor.y = platform_rect.top - self.actor.height // 2
                self.velocity_y = 0
                self.on_ground = True
                landed = True
                if self.state == "jump":
                    self.state = "idle"
                break

        if not landed:
            if self.actor.y >= GROUND_Y_CHARACTER:
                self.actor.y = GROUND_Y_CHARACTER
                self.velocity_y = 0
                self.on_ground = True
            else:
                self.on_ground = False

    def update_animation(self):
        if self.invulnerable:
            self.actor.image = "hero/hero_hit"
            return

        if self.state == "jump":
            self.actor.image = "hero/hero_jump"
        elif self.state == "run":
            self.frame_counter += 1
            if self.frame_counter % 10 == 0:
                self.current_frame = (self.current_frame + 1) % len(self.run_frames)
                base_image = self.run_frames[self.current_frame]
                self.actor.image = base_image if self.facing_right else base_image + "_left"
        else:
            self.actor.image = "hero/hero_idle"

        self.actor.flip_h = not self.facing_right

    def draw(self):
        if self.visible:
            self.actor.draw()

    def update(self):
        self.apply_gravity()
        self.check_platform_collision()
        self.update_animation()

        if self.on_ground and self.state != "jump":
            self.state = "idle"

        if self.invulnerable:
            self.invulnerable_timer -= 1
            if self.invulnerable_timer <= 0:
                self.invulnerable = False
                self.visible = True
            else:
                if self.invulnerable_timer % 10 == 0:
                    self.visible = not self.visible

    def collides_with(self, enemy):
        return self.actor.colliderect(enemy.actor)

    def take_damage(self):
        if not self.invulnerable:
            self.health -= 1
            self.invulnerable = True
            self.invulnerable_timer = HERO_INVULNERABLE_TIME
            print(f"Herói levou dano! Vidas restantes: {self.health}")
            if self.health <= 0:
                print("Game Over")
                return True
        return False