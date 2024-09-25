import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf

def run_game():
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(game_settings.size)
    pygame.display.set_caption('Alien Invasion')
    stats = GameStats(game_settings)

    ship = Ship(game_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(game_settings, screen, ship, aliens)

    while True:
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(game_settings, screen, ship, aliens, bullets)
        gf.update_aliens(game_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(game_settings, screen, ship, aliens, bullets)

run_game()