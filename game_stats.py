class GameStats():
    def __init__(self, settings):
        self.settings = settings
        self.reset_status()
        
    def reset_status(self):
        self.ships_left = self.settings.ship_limit