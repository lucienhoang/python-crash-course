import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting positions."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image.
        self.image = pygame.image.load("images/ship.png")

        # Calculate the new width.
        width = self.image.get_width() * ai_settings.sprite_scale

        # Calculate the new height.
        height = self.image.get_height() * ai_settings.sprite_scale

        # Resize the ship image.
        self.image = pygame.transform.smoothscale(self.image, (width, height))

        # Store the ship’s rect in self.rect.
        self.rect = self.image.get_rect()

        # Store the screen’s rect in self.screen_rect
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx  #  The x-coordinate of the ship’s center match the centerx attribute of the screen’s rect.
        self.rect.bottom = self.screen_rect.bottom  # The y-coordinate of the ship’s bottom equal to the value of the screen rect’s bottom attribute.

        # Store a decimal value for both x and y axes.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        # Draw self.image onto self.screen at the position self.rect.
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
