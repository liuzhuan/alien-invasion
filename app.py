import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.size)
    pygame.display.set_caption('Alien Invasion')

    ship = Ship(screen)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(game_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

    pygame.quit()

run_game()