class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_status()
        self.game_active = True
        
    def reset_status(self):
        self.ships_left = self.settings.ship_limit