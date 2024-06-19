import math

import gui
import sound

angle = math.radians(80)

collision_detected = False
miss_collision_detected = False
shoot_status = False
miss_shoot_left_status = False
miss_shoot_right_status = False

score = 0
misses = 0

def move_ball(shoot_status,miss_shoot_left_status,miss_shoot_right_status):
    if gui.ball_rect.centery <= 165:
        shoot_status = False
        miss_shoot_left_status = False
        miss_shoot_right_status = False
        gui.ball_rect.centerx = 769
        gui.ball_rect.centery = 524
    if shoot_status == True:
        gui.ball_rect.y -= 10
    if miss_shoot_left_status == True:
        gui.ball_rect.x -= 10*math.cos(angle)
        gui.ball_rect.y -= 10*math.sin(angle)
    if miss_shoot_right_status == True:
        gui.ball_rect.x += 10*math.cos(angle)
        gui.ball_rect.y -= 10*math.sin(angle)
    return shoot_status,miss_shoot_left_status,miss_shoot_right_status

def ball_scored(score,misses,collision_detected,miss_collision_detected,game_active,replay_menu):
    if gui.ball_rect.collidepoint((770,171)):
        if not collision_detected == True:
            sound.cheer.play()
            score += 1
            collision_detected = True
    elif gui.ball_rect.collidepoint((840,171)) or gui.ball_rect.collidepoint((700,171)) :
        if not miss_collision_detected == True:
            sound.boo.play()
            misses += 1
            miss_collision_detected = True
    else:
        collision_detected = False
        miss_collision_detected = False
    if misses == 5 :
        game_active = False
        replay_menu = True
    return score,misses,collision_detected,miss_collision_detected,game_active,replay_menu