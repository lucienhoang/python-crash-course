import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the feet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image.
        self.image = pygame.image.load("images/alien.png")

        # Calculate the new width and height.
        width = self.image.get_width() * ai_settings.sprite_scale
        height = self.image.get_height() * ai_settings.sprite_scale

        # Resize the ship image.
        self.image = pygame.transform.smoothscale(self.image, (width, height))

        # Set rect attribute.
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact positions.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the alien right."""
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
