import gui
import initialize

def display_play_again(screen):
        screen.blit(gui.background,(0,0))
        screen.blit(gui.menu,gui.menu_rect)
        screen.blit(initialize.play_again_button,initialize.play_again_button_rect)
def display_score(screen,score):
        end_text = gui.text_font2.render("Your Score : " + str(score) , False, 'Black')
        screen.blit(end_text,(705,280))