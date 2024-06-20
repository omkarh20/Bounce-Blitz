import pygame

from sys import exit

clock = pygame.time.Clock()
pygame.init()

text_font3 = pygame.font.Font('Resources\Bauhaus-93\Bauhaus 93 Regular.ttf',40)
play_again_button = text_font3.render("Play Again", False, 'White')
play_again_button_rect = play_again_button.get_rect(center = (830,350))

def window():
    display_dimension = (1550,800)
    screen = pygame.display.set_mode(display_dimension)
    pygame.display.set_caption("Bounce Blitz")
    return screen

def quit(event):
    if event.type == pygame.QUIT :
        pygame.quit()
        exit()

def reset(event,game_active,replay_menu,score,misses):
    if game_active == False and event.type == pygame.MOUSEBUTTONDOWN and play_again_button_rect.collidepoint(event.pos) :
          game_active = True
          replay_menu = False
          misses = 0
          score = 0
    return game_active,replay_menu,score,misses

def time():
    clock.tick(60)
    