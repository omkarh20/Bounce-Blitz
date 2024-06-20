import pygame

import gui

score = 0
misses = 0

score_text = gui.text_font1.render("Score : 0", False, 'White')
score_rect = score_text.get_rect(center = (1075,35))
misses_text = gui.text_font1.render("Misses : 0/5", False, 'White')
misses_rect = misses_text.get_rect(center = (475,35))

def display_score(screen,score):
    score_text = gui.text_font1.render("Score : " + str(score), False, 'White')
    score_rect = score_text.get_rect(center = (1075,35))
    screen.blit(score_text,score_rect)

def display_misses(screen,misses):
    misses_text = gui.text_font1.render("Misses : " + str(misses) + "/5", False, 'White')
    misses_rect = misses_text.get_rect(center = (475,35))
    screen.blit(misses_text,misses_rect)