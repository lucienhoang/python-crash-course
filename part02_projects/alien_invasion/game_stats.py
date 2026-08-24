class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics for Alien Invasion."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start Alien Invasion is an active state.
        self.game_active = True

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_settings.ship_limit
