# .\.venv\Scripts\Activate.ps1

import pygame  # The pygame module contains the functionality to make a game.  # noqa: I001
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
import game_functions as gf


def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    clock = pygame.time.Clock()

    # Create an instance to store game statistics and create a score board.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Creating the fleet of alien.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(
            ai_settings, screen, stats, sb, play_button, ship, aliens, bullets
        )

        if stats.game_active:
            # Update ship.
            ship.update()
            # Update bullets.
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            # Update aliens.
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        # Update screen.
        gf.update_screen(
            ai_settings, screen, stats, sb, ship, aliens, bullets, play_button
        )

        clock.tick(60)


run_game()
