import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
def run_game():
#initialize pygame ,settings,and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Make the play  button.
    play_button=Button(ai_settings,screen,"PLAY")

    #Create an instance to stora game statistics and create a scoreboard.
    stats=GameStats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)

    # Make a ship,a group of bullets,and a group of aliens.

    #Make a ship
    ship = Ship(ai_settings,screen)

    #Make a group to store bullets in.
    bullets=Group()

    # Make a group to store group of aliens.
    aliens=Group()

    # create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #set the background color.
    bg_color = (230,230,230)

    #Make an alien.
    alien=Alien(ai_settings,screen)

    #Create the fleet of aliens.
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #start the main loop for the game
    while True:
         gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)

         if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

         gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)

run_game()