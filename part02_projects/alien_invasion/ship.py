import pygame


class Ship:
    def __init__(self, screen):
        """Initialize the ship and set its starting positions."""
        self.screen = screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load(
            "images/ship.bmp"
        )  #  returns a surface representing the ship
        self.rect = self.image.get_rect()  # Store the ship’s rect in self.rect
        self.screen_rect = (
            self.screen.get_rect()
        )  # Store the screen’s rect in self.screen_rect

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx  #  The x-coordinate of the ship’s center match the centerx attribute of the screen’s rect.
        self.rect.bottom = self.screen_rect.bottom  # The y-coordinate of the ship’s bottom equal to the value of the screen rect’s bottom attribute.

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
