import pygame

bg_music = pygame.mixer.Sound('Resources/bg_music.mp3')
bg_music.set_volume(0.5)
cheer = pygame.mixer.Sound('Resources/crowd_cheer.mp3')
cheer.set_volume(0.3)
boo = pygame.mixer.Sound('Resources/crowd_boo.mp3')
boo.set_volume(0.3)

def play_music():
    bg_music.play(loops = -1)

