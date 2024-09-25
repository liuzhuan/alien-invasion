class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_size = (60, 60)
        self.ship_speed_factor = 1.5

        self.alien_size = 60, 60
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 5
        self.fleet_direction = 1

        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 'purple'
        self.bullets_allowed = 3
    
    @property
    def size(self):
        return (self.screen_width, self.screen_height)