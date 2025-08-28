import os

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
       
        # High score should never be reset.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save the highest score in a text file"""
        with open("high_score.txt", "w") as f:
            f.write(str(self.high_score))

    def load_high_score(self):
        if os.path.exists("high_score.txt"):
            with open("high_score.txt", "r") as f:
                return int(f.read())
        else:
            return 0
        
        
