# import the pygame module, so you can use it
import pygame
# import random to randomly place food
import random
# import time to wait before closing the game
import time
# import module scores
from Scores import *
 
# initialize the pygame module
pygame.init()
# load and set the logo
logo = pygame.image.load("logo.jpg")
pygame.display.set_icon(logo)
pygame.display.set_caption("Snake game by Theo Botella")
     
# some colors for our game
green = (50,205, 50)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
grey = (128, 128, 128)

# create a surface on screen that has the size of 500 x 500
screen_w = 500
screen_h = 500
screen = pygame.display.set_mode((screen_w, screen_h))

# font style for message and score
font_style = pygame.font.SysFont("chiller", 100)
score_font = pygame.font.SysFont("chiller", 35)

# message end game display on screen
def message(msg,color, font_style):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_w//2-140, screen_h//2-80])


# define a main function
def main():
     
    # create the snake (centered) 
    x_head = screen_w//2
    y_head = screen_h//2
    
    x_change = 0
    y_change = 0
        
    # define a variable to control the main loop
    running = True
     
    clock = pygame.time.Clock()

    def new_food():
        foodx = round(random.randrange(10, screen_w - 10) / 10.0) * 10.0
        foody = round(random.randrange(10, screen_h - 10) / 10.0) * 10.0
        return (foodx, foody)
    
    food = new_food()
    foodx = food[0]
    foody = food[1]

    score = 0

    # store the directions to get the previous direction and make reverse impossible
    directions = ['']

    snake_body = []
    snake_len = 0
    # main loop
    while running:
    
        # Gets all event from the event queue (created by pygame.KEYDOWN)
        for event in pygame.event.get():
            
            # when key is pressed
            if event.type == pygame.KEYDOWN:
                # set x,y change to 0
                x_change = 0
                y_change = 0
                # if key UP is pressed move on y axis
                # if previous direction was opposite direction, continue on this direction
                if event.key == pygame.K_UP and directions[-1] != "down":
                    x_change += 0
                    y_change += -10
                    directions.append('up')
                elif event.key == pygame.K_UP and directions[-1] == 'down':
                    x_change += 0
                    y_change += 10    
                    
                elif event.key == pygame.K_DOWN and directions[-1] != "up":
                    x_change += 0
                    y_change += 10
                    directions.append('down')
                elif event.key == pygame.K_DOWN and directions[-1] == "up":
                    x_change += 0
                    y_change += -10

                elif event.key == pygame.K_RIGHT and directions[-1] != "left":
                    x_change += 10
                    y_change +=0
                    directions.append('right')
                elif event.key == pygame.K_RIGHT and directions[-1] == "left":
                    x_change += -10
                    y_change += 0

                elif event.key == pygame.K_LEFT and directions[-1] != "right":
                    x_change += -10
                    y_change += 0
                    directions.append('left')
                elif event.key == pygame.K_LEFT and directions[-1] == "right":
                    x_change += 10
                    y_change +=0
                
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        

        # position updated (move)
        x_head += x_change
        y_head += y_change
        
        # screen filled in black to display only the new position of the snake
        screen.fill(black)
        #pygame.draw.rect(screen, white, [x_head, y_head, 10, 10])

        # create bondaries
        width = 1
        boundaries = [(0-width, 0), (0, screen_h-width), (0 ,0), (screen_w, 0),
                    (screen_w-width, 0), (screen_w-width, screen_h-width), 
                    (0, screen_h-width), (screen_w-width, screen_h-width)]

        pygame.draw.lines(screen, red, False, boundaries, 1)
        
        # bondaries
        if (x_head<0 or x_head>screen_w or y_head<0 or y_head>screen_h):
            running = False
            save_score(score)
            message("WASTED",red, font_style)
        
        #food
        pygame.draw.rect(screen, green, [int(foodx), int(foody), 10, 10])

        # if food is eaten, create new food and increment score
        if (x_head==foodx and y_head==foody):
            food = new_food()
            foodx = food[0]
            foody = food[1]
            score += 1
            get_best_score('score.txt')
            snake_len += 1
        
        # store position of snake_head every iteration
        snake_head = []
        snake_head.append(x_head)
        snake_head.append(y_head)
        
        # append ([x_head, y_head]) the position of the snake_head to the snake body
        snake_body.append(snake_head)
        
        # for each previous position of the snake, draw the body of the snake
        for xy in snake_body:
            pygame.draw.rect(screen, grey, [xy[0], xy[1], 10, 10])    
        
        # delete the old position to keep only a body of the good length
        if (len(snake_body) > snake_len):
            # delete the duplicated head so we start with only one snake block 
            del snake_body[0]
       
        # game over if head of snake touch its body
        # last block of body has same x,y than head when created
        for xy in snake_body[:-1]:   
            if (snake_head == xy):
                running = False
                save_score(score)
                message("WASTED",red, font_style)

        current_score(score)
        display_best_score('score.txt')
        # update the entire screen with a timeframe of 5 frames per secondes 
        pygame.display.update()
        # increase frames per sec to increase difficulty
        clock.tick(15)
      
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()