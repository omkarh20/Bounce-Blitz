import pygame

import gui

def display_play(screen,event,start_menu,difficulty_menu):
    screen.blit(gui.background,(0,0))
    screen.blit(gui.menu,gui.menu_rect)
    screen.blit(gui.title_text1,gui.title1_rect)
    screen.blit(gui.play_button,gui.play_button_rect)
    if event.type == pygame.MOUSEBUTTONDOWN :
        if gui.play_button_rect.collidepoint(event.pos) :
            start_menu = False
            difficulty_menu = True
    return start_menu,difficulty_menu

def display_difficulty(screen):
    screen.blit(gui.background,(0,0))
    screen.blit(gui.menu,gui.menu_rect)
    screen.blit(gui.title_text1,gui.title1_rect)
    screen.blit(gui.difficulty_button,gui.difficulty_button_rect)
    screen.blit(gui.easy_button,gui.easy_button_rect)
    screen.blit(gui.medium_button,gui.medium_button_rect)
    screen.blit(gui.hard_button,gui.hard_button_rect)



