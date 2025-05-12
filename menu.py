# type: ignore
from pgzero.builtins import Rect
from pgzero.screen import Screen
from pgzero.builtins import music

class Menu:
    def __init__(self, width, height):
        self.is_sound_on = True
        self.window = {'width': width, 'height': height}
        self.button_start = Rect((self.window['width'] // 2 - 100, 200), (200, 50))
        self.button_sound = Rect((self.window['width'] // 2 - 100, 280), (200, 50))
        self.button_exit = Rect((self.window['width'] // 2 - 100, 360), (200, 50))

    def draw(self, screen: Screen):
        screen.fill((30, 30, 60))
        screen.draw.text("Main Menu", center=(self.window['width'] // 2, 100), fontsize=60, color=(255, 255, 255))

        screen.draw.filled_rect(self.button_start, (180, 180, 180))
        screen.draw.text("Start Game", center=self.button_start.center, color=(0, 0, 0))

        sound_label = "Sound: ON" if self.is_sound_on else "Sound: OFF"
        screen.draw.filled_rect(self.button_sound, (180, 180, 180))
        screen.draw.text(sound_label, center=self.button_sound.center, color=(0, 0, 0))

        screen.draw.filled_rect(self.button_exit, (180, 180, 180))
        screen.draw.text("Exit", center=self.button_exit.center, color=(0, 0, 0))

    def on_mouse_down(self, pos):
        if self.button_start.collidepoint(pos):
            print("Start the game")
            if self.is_sound_on:
                music.play('background_music')
        elif self.button_sound.collidepoint(pos):
            self.is_sound_on = not self.is_sound_on
            print(f"Sound {'ON' if self.is_sound_on else 'OFF'}")
            if self.is_sound_on:
                music.play('background_music')
            else:
                music.stop()
        elif self.button_exit.collidepoint(pos):
            exit()