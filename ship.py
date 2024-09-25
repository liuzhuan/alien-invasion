import pygame
from settings import Settings

class Ship():
    def __init__(self, screen):
        game_settings = Settings()

        self.screen = screen
        self.image = pygame.image.load('images/ship.png').convert_alpha()
        # 调整飞船尺寸
        self.image = pygame.transform.scale(self.image, game_settings.ship_size)
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1