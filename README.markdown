# Platform Game

A 2D platform game built using Python and Pygame Zero. The game features a hero character navigating through platforms, avoiding enemies, and overcoming challenges.

## Features

- **Hero Character**: Move, jump, and interact with the environment.
- **Enemies**: AI-controlled enemies with patrol behavior.
- **Platforms**: Static platforms for the hero to navigate.
- **Main Menu**: Start the game, toggle sound, or exit.
- **Game Over Screen**: Displays when the hero loses all health.
- **Background Music**: Dynamic music that can be toggled on/off.

## File Structure

- `settings.py`: Contains game settings like dimensions, gravity, and hero/enemy attributes.
- `menu.py`: Implements the main menu with buttons for starting the game, toggling sound, and exiting.
- `main.py`: The entry point of the game, managing screen transitions and game states.
- `hero.py`: Defines the hero character's behavior, animations, and interactions.
- `enemy.py`: Defines enemy behavior, including movement and animations.
- `game.py`: Manages the game logic, including platform generation, hero-enemy interactions, and game updates.

## How to Run

1. Install [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/).
2. Clone this repository.
3. Run the `main.py` file using the command:
   ```bash
   pgzrun main.py