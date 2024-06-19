import pygame

import gui

def selection(event,difficulty_menu,game_active,difficulty_mode):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if gui.easy_button_rect.collidepoint(mouse_pos):
                game_active = True
                difficulty_menu = False
                difficulty_mode = 'Easy'
            if gui.medium_button_rect.collidepoint(mouse_pos):
                game_active = True
                difficulty_menu = False
                difficulty_mode = 'Medium'
            if gui.hard_button_rect.collidepoint(mouse_pos):
                game_active = True
                difficulty_menu = False
                difficulty_mode = 'Hard'
        return difficulty_menu,game_active,difficulty_mode

def change_difficulty(difficulty_mode):
    if difficulty_mode == 'Easy':
        dot_speed = 12
    elif difficulty_mode == 'Medium':
        dot_speed = 15
    else :
        dot_speed = 20
    return dot_speed
