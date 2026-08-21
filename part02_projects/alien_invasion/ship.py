import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting positions."""
        self.screen = screen
        self.ai_settings = ai_settings

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

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
