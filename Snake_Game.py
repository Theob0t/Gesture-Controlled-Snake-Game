# import the pygame module, so you can use it
import pygame
# import random to randomly place food
import random
# import time to wait before closing the game
import time
# import sys to exit
import sys


def new_food():
        foodx = round(random.randrange(10, screen_w - 10) / 10.0) * 10.0
        foody = round(random.randrange(10, screen_h - 10) / 10.0) * 10.0
        return (foodx, foody)

# current score display on screen 
def current_score(score):
    value = score_font.render("Score: " + str(score), True, red)
    screen.blit(value, [5, 0])
    return score

# save score in file ./data/score.txt
def save_score(score):
    final_score = ','+str(score)
    with open('./data/score.txt', 'a', encoding = 'utf-8') as file:
        file.write(f'{final_score}')
    return final_score

# read ./data/score.txt and select best score 
def get_best_score(file):
    with open('./data/score.txt', 'r+', encoding = 'utf-8') as file:
        for line in file:
            scores_best_score = line.strip().split(",")
        bs = list([int(x) for x in scores_best_score])
    if (len(bs) <=0):
        return '0'
    if (len(bs) > 0):
        bs.sort()
        return bs[-1]
    
# best score display on screen  
def display_best_score(file, score):
    best_score = str(get_best_score(file))
    if int(best_score) < int(score):
        best_score = int(score)
    value = score_font.render("Best Score: " + str(best_score), True, red)
    screen.blit(value, [330, 0])
    return

# message end game display on screen
def message(msg,color, font_style, x, y):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [x, y])

def button(screen, color, x, y, w, h, msg):
    # draw the button with the message
    pygame.draw.rect(screen, color, [x, y, w , h])
    message(msg, black, score_font, x+25, y+5)

def select_level():
    # get position of the mouse and every click
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # easy = 15f/s, hard = 25f/s
    level = 0 
    # adjust level depending on button clicked
    # run mainloop once level is chosen
    if ((205+110 > mouse[0] > 205) and (250+45 > mouse[1] > 45)):
        if (click[0] == 1 and mouse[1]<300):
            level = 15

    if  ((205+110 > mouse[0] > 205) and (350+45 > mouse[1] > 45)):
        if ((click[0] == 1) and (mouse[1]>300)): 
            level = 25
    
    return level       
           
def menu():
    menu = True
    clock = pygame.time.Clock()
    level = 0
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # change the value to False, to exit the loop
                menu = False
                pygame.display.quit()
                sys.exit()
           
            screen.fill(grey)
            message('Snake Game', green, font_style, screen_w//2-165, screen_h//2-200)
            message('by Theob0t', green, score_font, screen_w//2-50, screen_h//2-90)

            button(screen, (200,200,200), 205, 250, 110 , 45, 'EASY')
            button(screen, (120,120,120), 205, 350, 110 , 45, 'HARD') 

            level = select_level()
            if (level != 0):
                menu = False   
            pygame.display.update()
            clock.tick(15)

    return level

# define a main function
def game(level):
     
    # create the snake (centered) 
    x_head = screen_w//2
    y_head = screen_h//2
    
    x_change = 0
    y_change = 0
        
    # define a variable to control the main loop
    running = True
     
    clock = pygame.time.Clock()
    
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
                pygame.display.quit()
                sys.exit()


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
            message("WASTED",red, font_style, screen_w//2-140, screen_h//2-80)
        
        #food
        pygame.draw.rect(screen, green, [int(foodx), int(foody), 10, 10])

        # if food is eaten, create new food and increment score
        if (x_head==foodx and y_head==foody):
            food = new_food()
            foodx = food[0]
            foody = food[1]
            score += 1
            get_best_score('./data/score.txt')
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
                message("WASTED",red, font_style, screen_w//2-140, screen_h//2-80)
                

        current_score(score)
        display_best_score('./data/score.txt', score)
        # update the entire screen with a timeframe of 5 frames per secondes 
        pygame.display.update()
        # increase frames per sec to increase difficulty
        clock.tick(level)
    end_game(level)
    return 

def end_game(level):
    wait = True
    while wait:
        message("SPACE  to  Replay",white, over_style, screen_w//2-70, screen_h//2+50)
        message("ENTER  to   MENU",white, over_style, screen_w//2-70, screen_h//2+90)
        message("  Q    to   QUIT",white, over_style, screen_w//2-70, screen_h//2+130)
        pygame.display.update()  
        
        time.sleep(0.1)
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    wait = False
                    game(level)

                elif (event.key == pygame.K_RETURN):
                    wait = False
                    main()

                elif (event.key == pygame.K_q):
                    wait = False
                    pygame.display.quit()
                    sys.exit()
            
            if (event.type == pygame.QUIT):
                # change the value to False, to exit the loop
                wait = False
                pygame.display.quit()
                sys.exit()

    return

def main():
        # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("./data/logo.jpg")
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
    over_style = pygame.font.SysFont("dejavusans", 25)

    scores = []
    bs = []

    level = menu() 
    game(level)
    return

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("./data/logo.jpg")
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
    over_style = pygame.font.SysFont("dejavusans", 25)

    scores = []
    bs = [] 
    main()
    