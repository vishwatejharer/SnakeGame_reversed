import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#Background image
bgimg=pygame.image.load("2.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
bg=pygame.image.load("3.jpg")
bg=pygame.transform.scale(bg,(screen_width,screen_height)).convert_alpha()
b=pygame.image.load("v.jpg")
b=pygame.transform.scale(b,(150,250)).convert_alpha()
# Game Title
pygame.display.set_caption("SnakesWithVishu")
pygame.display.update()

font = pygame.font.SysFont(None, 55)

fps = 30
clock = pygame.time.Clock()

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_lst,snake_size):
    for x,y in snk_lst:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def wellcome():
    exit_game=False
    pygame.mixer.music.load('m1.mp3')
    pygame.mixer.music.play()
    while not exit_game:

        gameWindow.fill(black)
        gameWindow.blit(bgimg, (0, 0))
        gameWindow.blit(b, (int(screen_width)/2-75, 100))
        text_screen("Snakes by VISHWATEJ",(212,175,55),220,400)
        text_screen("Press space to play",(255,223,0),240,500)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    #pygame.mixer.music.load('music.mp3')
                    #pygame.mixer.music.play()
                    #pygame.mixer.music.load('m1.mp3')
                    #pygame.mixer.music.play()
                    pygame.mixer.music.load('m2.mp3')
                    pygame.mixer.music.play()
                    #pygame.mixer.music.load('m3.mp3')
                    #pygame.mixer.music.play()

                    game_loop()
        pygame.display.update()
        clock.tick(fps)


def game_loop():

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(40, screen_width - 40)
    food_y = random.randint(40, screen_height - 40)
    score = 0
    snake_size = 30

    snk_lst = []
    snk_length = 1
    #check if text file exists
    if not os.path.exists(("highscore.txt")):
        with open("highscore.txt","w")as f:
            f.write("0")
    with open("highscore.txt","r") as f:
        highscore=f.read()

    # Game Loop
    while not exit_game:

        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(white)
            gameWindow.blit(bg, (0, 0))
            text_screen("Game Over! Press Enter To Continue",(0,255,0),100,550)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        wellcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x =-init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y =-init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x-food_x)<snake_size//2  and abs(snake_y-food_y)<snake_size//2:
                score+=10
                food_x = random.randint(40, screen_width - 40)
                food_y = random.randint(40, screen_height - 40)
                snk_length+=5
                if score > int(highscore):
                    highscore=score

            gameWindow.fill(black)

            text_screen("Score: " + str(score) + "  Highscore: "+str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow,(0,0,255), [food_x, food_y, snake_size, snake_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_lst.append(head)

            if len(snk_lst)>snk_length:
                del snk_lst[0]

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if head in snk_lst[:-1]:
                game_over=True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow,red,snk_lst,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
wellcome()