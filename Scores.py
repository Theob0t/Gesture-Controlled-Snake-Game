# import the pygame module, so you can use it
import pygame
# import random to randomly place food
import random
# import time to wait before closing the game
import time


# initialize the pygame module
pygame.init()
# load and set the logo
logo = pygame.image.load("logo.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Snake game by Theo Botella")
     
scores = []

# some colors for our game
blue=(0,0,255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# create a surface on screen that has the size of 500 x 500
screen_w = 500
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))

# font style for message and score
font_style = pygame.font.SysFont("chiller", 100)
score_font = pygame.font.SysFont("chiller", 35)

# current score display on screen 
def current_score(score):
    value = score_font.render("Score: " + str(score), True, red)
    screen.blit(value, [5, 0])
    return score

# save score in file score.txt
def save_score(score):
    final_score = '00' + str(score)
    with open('score.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{final_score}')
    return final_score

# read score.txt and select best score 
scores_best_score = []
def get_best_score(file):
    with open('score.txt', 'r+', encoding = 'utf-8') as file:
        for line in file:
            scores_best_score.append(line) 
    if (len(scores_best_score) <=0):
        return 0
    else:
        scores_best_score.sort()
        return scores_best_score[-1]
    
# best score display on screen
bs = []    
def display_best_score(file):
    best_score = str(get_best_score(file))
    for l in best_score:
        bs.append(l)
    bs.sort()
    best_score = bs[-1]
    value = score_font.render("Best Score: " + str(best_score), True, red)
    screen.blit(value, [330, 0])
    return