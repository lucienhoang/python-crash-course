class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Sprite settings
        self.sprite_scale = 0.4

        # Ship settings
        self.ship_speed_factor = 0.8
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed_factor = 0.8
        self.fleet_drop_speed = 10
        # fleet direction of represents right; -1 represent left.
        self.fleet_direction = 1
