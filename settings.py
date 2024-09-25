class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_size = (80, 80)
        self.ship_speed_factor = 1.5
    
    @property
    def size(self):
        return (self.screen_width, self.screen_height)