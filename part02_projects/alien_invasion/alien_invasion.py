# .\.venv\Scripts\Activate.ps1

import pygame  # The pygame module contains the functionality to make a game.  # noqa: I001
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Creating the fleet of alien.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update ship.
        ship.update()
        # Update bullets.
        gf.update_bullets(bullets)
        # Update aliens.
        gf.update_aliens(aliens)
        # Update screen.
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
