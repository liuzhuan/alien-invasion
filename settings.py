class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        self.ship_size = (60, 60)
        self.ship_limit = 3

        self.alien_size = 60, 60
        self.fleet_drop_speed = 10

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 'purple'
        self.bullets_allowed = 3

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    @property
    def size(self):
        return (self.screen_width, self.screen_height)
    
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale