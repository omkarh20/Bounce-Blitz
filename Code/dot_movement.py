import pygame

import gui

dot_radius = 30
dot_direction = 1
dot = pygame.transform.scale(gui.ball,(60,60))
dot_rect = gui.ball.get_rect(center = (755,705))

flag = False

def move_dot(screen,dot_speed,dot_direction):
    dot_rect.x += dot_speed*dot_direction
    if dot_rect.x - dot_radius <= 575 or dot_rect.x + dot_radius >= 930:
        dot_direction *= -1
    screen.blit(dot,dot_rect)
    return dot_direction

def shoot(shoot_status,miss_shoot_left_status,miss_shoot_right_status,flag):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] :
        if 725<=dot_rect.x <= 775 and not flag:
            shoot_status = True 
            flag = True
        elif 594 <= dot_rect.x < 710 and not flag:
            miss_shoot_left_status = True
            flag = True
        elif 805 < dot_rect.x <= 975 and not flag: 
            miss_shoot_right_status = True
            flag = True
        else:
            pass
    else:
        flag = False
    return shoot_status,miss_shoot_left_status,miss_shoot_right_status,flag