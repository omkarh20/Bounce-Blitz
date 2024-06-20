import pygame

import initialize
import start
import difficulty
import gui
import stats
import dot_movement
import ball
import sound
import replay

pygame.init()

screen = initialize.window()

game_active = False
start_menu = True
difficulty_menu = False
replay_menu = False
difficulty_mode = 'Easy'

sound.play_music()

dot_direction = 1

shoot_status,miss_shoot_left_status,miss_shoot_right_status,flag = \
    ball.shoot_status,ball.miss_shoot_left_status,ball.miss_shoot_right_status,dot_movement.flag

score,misses = stats.score,stats.misses

collision_detected,miss_collision_detected = ball.collision_detected,ball.miss_collision_detected

while True:
    for event in pygame.event.get():
        initialize.quit(event)
        game_active,replay_menu,misses,score = initialize.reset(event,game_active,replay_menu,misses,score)
        if start_menu :
            start_menu,difficulty_menu = start.display_play(screen,event,start_menu,difficulty_menu)
    if difficulty_menu :
        start.display_difficulty(screen)
        difficulty_menu,game_active,difficulty_mode = \
            difficulty.selection(event,difficulty_menu,game_active,difficulty_mode)
        dot_speed = difficulty.change_difficulty(difficulty_mode)
    if game_active :
        gui.draw_images(screen)
        gui.draw_text(screen)

        stats.display_score(screen,score)
        stats.display_misses(screen,misses)

        dot_direction = dot_movement.move_dot(screen,dot_speed,dot_direction)
        shoot_status,miss_shoot_left_status,miss_shoot_right_status,flag = \
            dot_movement.shoot(shoot_status,miss_shoot_left_status,miss_shoot_right_status,flag)

        shoot_status,miss_shoot_left_status,miss_shoot_right_status = \
            ball.move_ball(shoot_status,miss_shoot_left_status,miss_shoot_right_status)

        score,misses,collision_detected,miss_collision_detected,game_active,replay_menu = ball.ball_scored\
            (score,misses,collision_detected,miss_collision_detected,game_active,replay_menu)

    if replay_menu :
        replay.display_play_again(screen)
        replay.display_score(screen,score)
        
    pygame.display.update()
    initialize.time()
