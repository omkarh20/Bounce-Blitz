import pygame
 
from initialize import window

pygame.init()

window()

background = pygame.image.load('Resources/background.jpg').convert()
background = pygame.transform.smoothscale(background,(1550,800))

menu = pygame.image.load('Resources/menu.png').convert_alpha()
menu = pygame.transform.smoothscale(menu,(650,650))
menu_rect = menu.get_rect(center = (770,385))

court = pygame.image.load('Resources/court.jpg').convert()
court = pygame.transform.scale(court,(800,800))

player_orange = pygame.image.load('Resources/playerorange.png').convert_alpha()
player_orange = pygame.transform.scale(player_orange,(70,125))
player_rect1 = player_orange.get_rect(center = (769,545))
player_rect4 = player_orange.get_rect(center = (570,515))
player_rect5 = player_orange.get_rect(center = (985,515))

player_blue = pygame.image.load('Resources/playerblue.png').convert_alpha()
player_blue = pygame.transform.scale(player_blue,(70,125))
player_rect2 = player_blue.get_rect(center = (570,650))
player_rect3 = player_blue.get_rect(center = (985,650))
player_rect6 = player_blue.get_rect(center = (985,390))

ball = pygame.image.load('Resources/ball.png').convert_alpha()
ball = pygame.transform.scale(ball,(40,40))
ball_rect = ball.get_rect(center = (769,524))

text_font1 = pygame.font.Font('Resources\Caveat\Caveat-VariableFont_wght.ttf',40)
text_font2 = pygame.font.Font('Resources\Bauhaus-93\Bauhaus 93 Regular.ttf',40)

title_text1 = text_font2.render("Bounce Blitz", False, 'Black')
title1_rect = title_text1.get_rect(center = (770,185))

title_text2 = text_font1.render("Bounce Blitz", False, 'White')
title2_rect = title_text2.get_rect(center = (750,35))

play_button = text_font2.render("Play", False, 'White')
play_button_rect = play_button.get_rect(center = (830,305))

difficulty_button = text_font2.render("Difficulty",False,'Black')
difficulty_button_rect = difficulty_button.get_rect(center = (790,310))

easy_button = text_font2.render("Easy",False,'White')
easy_button_rect = easy_button.get_rect(center = (830,350))

medium_button = text_font2.render("Medium",False,'White')
medium_button_rect = medium_button.get_rect(center = (830,390))

hard_button = text_font2.render("Hard",False,'White')
hard_button_rect = hard_button.get_rect(center = (830,445))

def draw_images(screen):
    screen.blit(background,(0,0))
    screen.blit(court,(375,0))
    screen.blit(ball,ball_rect)

    screen.blit(player_orange,player_rect1)
    screen.blit(player_blue,player_rect2)
    screen.blit(player_blue,player_rect3)
    screen.blit(player_orange,player_rect4)
    screen.blit(player_orange,player_rect5)
    screen.blit(player_blue,player_rect6)

    pygame.draw.rect(screen,'Black',(605,690,350,50))

def draw_text(screen):
    screen.blit(title_text2,title2_rect)