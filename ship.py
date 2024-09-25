import pygame

class Ship():
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        # 调整飞船尺寸
        self.image = pygame.transform.scale(self.image, self.settings.ship_size)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.settings.ship_speed_factor
        self.rect.centerx = self.center