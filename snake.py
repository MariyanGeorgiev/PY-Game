import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
green = (0, 255, 0)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (50, 255, 255)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

color_list = [white, yellow, green, black, red]
color_names = ["White", "Yellow", "Green", "Black", "Red"]
snake_color = white
food_color = green

def score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    dis.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

def color_menu(color_type):
    global snake_color
    global food_color
    color = color_list[0]
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    color = color_list[(color_list.index(color) - 1) % len(color_list)]
                elif event.key == pygame.K_DOWN:
                    color = color_list[(color_list.index(color) + 1) % len(color_list)]
                if event.key == pygame.K_RETURN:
                    if color_type == "snake":
                        snake_color = color
                    elif color_type == "food":
                        food_color = color
                    menu = False

        dis.fill(blue)
        title = font_style.render(color_type.capitalize() + " Color: ", True, white)
        selected_color = font_style.render(color_names[color_list.index(color)], True, color)
        dis.blit(title, (dis_width // 2 - 100, dis_height // 2 - 20))
        dis.blit(selected_color, (dis_width // 2 + 150, dis_height // 2 - 20))
        pygame.display.update()
        clock.tick(30)

def game_menu():
    menu = True
    selected = "start"

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected == "start":
                        selected = "quit"
                    elif selected == "snake_color":
                        selected = "start"
                    elif selected == "food_color":
                        selected = "snake_color"
                    elif selected == "quit":
                        selected = "food_color"
                elif event.key == pygame.K_DOWN:
                    if selected == "start":
                        selected = "snake_color"
                    elif selected == "snake_color":
                        selected = "food_color"
                    elif selected == "food_color":
                        selected = "quit"
                    elif selected == "quit":
                        selected = "start"

                if event.key == pygame.K_RETURN:
                    if selected == "start":
                        gameLoop()
                    elif selected == "snake_color":
                        color_menu("snake")
                    elif selected == "food_color":
                        color_menu("food")
                    if selected == "quit":
                        pygame.quit()
                        quit()

        dis.fill(blue)
        title = font_style.render("Snake Game", True, white)
        if selected == "start":
            text_start = font_style.render("Start", True, red)
        else:
            text_start = font_style.render("Start", True, white)
        if selected == "quit":
            text_quit = font_style.render("Quit", True, red)
        else:
            text_quit = font_style.render("Quit", True, white)
        if selected == "snake_color":
            text_snake_color = font_style.render("Snake Color", True, red)
        else:
            text_snake_color = font_style.render("Snake Color", True, white)
        if selected == "food_color":
            text_food_color = font_style.render("Food Color", True, red)
        else:
            text_food_color = font_style.render("Food Color", True, white)

        title_rect = title.get_rect()
        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
        snake_color_rect = text_snake_color.get_rect()
        food_color_rect = text_food_color.get_rect()

        dis.blit(title, (dis_width // 2 - (title_rect[2] // 2), 80))
        dis.blit(text_start, (dis_width // 2 - (start_rect[2] // 2), 300))
        dis.blit(text_snake_color, (dis_width // 2 - (snake_color_rect[2] // 2), 360))
        dis.blit(text_food_color, (dis_width // 2 - (food_color_rect[2] // 2), 420))
        dis.blit(text_quit, (dis_width // 2 - (quit_rect[2] // 2), 480))
        
        pygame.display.update()
        clock.tick(30)

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            game_menu()
            score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_s:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, food_color, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
