from menu import Menu
from game import Game
from pgzero.screen import Screen
from pgzero.builtins import music
import pgzrun
from settings import WIDTH, HEIGHT

current_screen = "menu"
screen: Screen
menu = Menu(width=WIDTH, height=HEIGHT)

def go_to_game_over():
    global current_screen
    current_screen = "game_over"

def restart_game():
    global current_screen
    game.reset()
    current_screen = "game"
    
game = Game(width=WIDTH, height=HEIGHT, on_game_over=go_to_game_over)

def draw():
    if current_screen == "menu":
        menu.draw(screen)
    elif current_screen == "game":
        game.draw(screen)
    elif current_screen == "game_over":
        screen.fill((0, 0, 0))
        screen.draw.text("Game Over", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=60, color="white")
        screen.draw.text("Click to return to menu", center=(WIDTH // 2, HEIGHT // 2 + 30), fontsize=30, color="gray")

def update():
    if current_screen == "game":
        game.update()

def on_key_down(key):
    if current_screen == "game":
        game.on_key_down(key)

def on_mouse_down(pos):
    global current_screen
    if current_screen == "menu":
        if menu.button_start.collidepoint(pos):
            current_screen = "game"
            if menu.is_sound_on:
                music.play('background_music')
        else:
            menu.on_mouse_down(pos)
    elif current_screen == "game_over":
        current_screen = "menu"
        game.reset()

def on_music_end():
    if current_screen == "game" and menu.is_sound_on:
        music.play("background_music")

pgzrun.go()
