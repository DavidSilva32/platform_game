# game.py
from hero import Hero
from enemy import Enemy
from pgzero.keyboard import keys, keyboard
from pgzero.screen import Screen
from pgzero.builtins import music, Rect
from settings import BACKGROUND_WIDTH, TILE_SIZE, GROUND_Y, ENEMY_COUNT
import random

class Game:
    def __init__(self, width, height, on_game_over=None):
        self.is_running = True
        self.window = (width, height)
        self.platforms = []
        self.reset()
        self.on_game_over = on_game_over

    def reset(self):
        self.platforms = self.build_platforms()
        self.hero = Hero(200, self.window[1] // 2, self.platforms)
        self.enemies = [
            Enemy(
                random.randint(0, self.window[0] - 50),
                random.randint(300, self.window[1] - 50),
                self.window[0]
            )
            for _ in range(ENEMY_COUNT)
        ]
        self.is_running = True

    def build_platforms(self):
        platform_y = self.window[1] - TILE_SIZE * 6

        tiles = [
            {'image': 'tiles/terrain_grass_horizontal_left', 'pos': (TILE_SIZE*1, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_middle', 'pos': (TILE_SIZE*2, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_middle', 'pos': (TILE_SIZE*3, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_middle', 'pos': (TILE_SIZE*4, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_right', 'pos': (TILE_SIZE*5, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_left', 'pos': (TILE_SIZE*13, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_middle', 'pos': (TILE_SIZE*14, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_middle', 'pos': (TILE_SIZE*15, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_middle', 'pos': (TILE_SIZE*16, platform_y)},
            {'image': 'tiles/terrain_grass_horizontal_right', 'pos': (TILE_SIZE*17, platform_y)}
        ]
        return [{'image': tile['image'], 'rect': Rect(tile['pos'], (TILE_SIZE, TILE_SIZE))} for tile in tiles]

    def draw(self, screen: Screen):
        screen.clear()
        for x in range(0, self.window[0], BACKGROUND_WIDTH):
            screen.blit('background/background_clouds', (x, 0))
            screen.blit('background/background_solid_cloud', (x, 256))
            screen.blit('background/background_fade_trees', (x, 512))

        for x in range(0, self.window[0], TILE_SIZE):
            screen.blit('tiles/terrain_grass_block_top', (x, GROUND_Y))

        for tile in self.platforms:
            screen.blit(tile['image'], tile['rect'].topleft)

        self.hero.draw()
        for enemy in self.enemies:
            enemy.draw()

    def update(self):
        if not self.is_running:
            return

        if keyboard.left:
            self.hero.move_left()
        if keyboard.right:
            self.hero.move_right()

        self.hero.update()
        self.hero.check_platform_collision()

        for enemy in self.enemies:
            enemy.update()
            if self.hero.collides_with(enemy):
                died = self.hero.take_damage()
                if died:
                    self.is_running = False
                    print("Parando o jogo")
                    music.stop()
                    if self.on_game_over:
                        self.on_game_over()
                    break

    def on_key_down(self, key):
        if key == keys.LEFT:
            self.hero.move_left()
        elif key == keys.RIGHT:
            self.hero.move_right()
        elif key == keys.SPACE:
            self.hero.jump()
