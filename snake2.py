"""
Author: Vedant, Wajiha Urooj
Last Revised: 5/23/2022
Summary: simple snake game using Pygame
"""
import pygame
import math
import random

pygame.init()
# The color values:
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
# parameters for the screen and the game:
dis_width = 600
dis_height = 400
adjust = 20
snake_block = adjust
# changes the size of the screen so that it is the proportional with the snake block
if dis_width % adjust > 0:
    while dis_width % adjust > 0:
        dis_width += 1

if dis_height % adjust > 0:
    while dis_height % adjust > 0:
        dis_height += 1

dis = pygame.display.set_mode((dis_width, dis_height))  # creates the display


pygame.display.set_caption('Snake Game by Edureka')  # creates the title for the display

clock = pygame.time.Clock()


font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):  # Creates different body color of the snake comparedd to head
    x = snake_list[-1]
    pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
    for y in snake_list[:-1]:
        pygame.draw.rect(dis, white, [y[0], y[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
def randfoodx(dis_width, snake_block):
    foodx = random.randrange(1 , round(dis_width / snake_block)-1) * snake_block
    return foodx
def randfoody(dis_height, snake_block):
    foody = random.randrange(1, round(dis_height / snake_block)-1) * snake_block
    return foody
def gameLoop():
    game_over = False
    game_close = False

    x1 = math.ceil(dis_width / 2)
    y1 = math.ceil(dis_height / 2)

    # Sets the coordinates of the snake according to the snake block:
    if x1 % adjust > 0:
        while x1 % adjust > 0:
            x1 += 1
            print(x1)

    if y1 % adjust > 0:
        while y1 % adjust > 0:
            y1 += 1
            print(y1)

    x1_change = 0  # change in the x coor

    y1_change = 0  # change in the y coor

    snake_List = []
    Length_of_snake = 1

    snake_speed = 5
    foodx = round(randfoodx(dis_width, snake_block))

    foody = round(randfoody(dis_height, snake_block))

    Truth = False
    selfeat = False
    while not game_over:

        while game_close:


            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            if selfeat:
                mesg = font_style.render("Ouch!!!!", True, black)
                dis.blit(mesg, [dis_width / 2, dis_height / 2])
            Your_score(Length_of_snake - 1)

            pygame.display.update()
            snake_speed = 5

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
            if Truth:
                pygame.draw.circle(dis, yellow, (x1, y1), 100)
                pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:

                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # checks if the snake hit the display wall
            Truth = True
            game_close = True
        x1 += x1_change  # changes the location of the snake
        y1 += y1_change
        dis.fill(blue)
        food = pygame.Rect(foodx, foody, snake_block, snake_block)
        pygame.draw.rect(dis, green, food)
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head) # stores the location of the snake head
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

            for x in snake_List[:-1]:
                if x == snake_Head:
                    selfeat = True
                    game_close = True

            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)

            pygame.display.update()


            if x1 == foodx and y1 == foody:  #  if the snake ate the food

                snake_speed = 5

                for r in range(snake_block, 0, -1):   # draws the effect if food is eaten
                    pygame.draw.circle(dis, red, (foodx, foody), r)
                pygame.display.update()
                # new food:
                foodx = round(randfoodx(dis_width, snake_block))
                foody = round(randfoody(dis_height, snake_block))
                Length_of_snake += 1

            clock.tick(snake_speed)
            snake_speed *= 1.01  # increases speed exponentially
            print(snake_speed)
    pygame.quit()
    quit()

gameLoop()