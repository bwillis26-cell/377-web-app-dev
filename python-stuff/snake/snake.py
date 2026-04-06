import pygame
import time
import random
from playsound3 import playsound
# import pygame_menu


pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.init()


white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600
dis_height = 400

surface = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')


clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
# Create the sound variables and load the sound files
eat_sound = pygame.mixer.Sound('eating.mp3') # Source: pixabay.com, free for commercial use, no attribution required
game_over_sound = pygame.mixer.Sound('game_over.mp3') #Source: pixabay.com, free for commercial use, no attribution required
skull = pygame.image.load('skull.png')  # Load the skull image for the game over screen

high_score = 0  # Initialize the high score variable

# Initialize the RGB values for the random background color
r = 50 
g = 50
b = 50


# Function to generate a random color by slightly changing the RGB values
def random_color():
    global r, g, b
    r += random.randint(-10, 10)
    g += random.randint(-10, 10)
    b += random.randint(-10, 10)
    r = max(50, min(205, r))
    g = max(50, min(205, g))
    b = max(50, min(205, b))
    return (r, g, b)

# Function to update the high score if the current score is greater than the high score
def update_high_score(score):
    global high_score
    if int(score) > high_score:
        high_score = score
    value = score_font.render("High Score: " + str(high_score), True, yellow)
    surface.blit(value, [dis_width - 250, 0])

def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    surface.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(surface, black, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    surface.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    global snake_speed
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
        i = 0
        while game_close == True:
            i += 1 # Allows the game over sound to play once and prevents it from repeating
            surface.fill(blue)
            if i == 1:  # Play the game over sound only once when the game is over
                game_over_sound.play(loops=0)  # Play the game over sound when the snake collides with itself or the wall
            skull_x = (dis_width - skull.get_width()) / 2
            skull_y = (dis_height - skull.get_height()) / 2 + 50
            skull_rect = skull.get_rect(center=(skull_x + skull.get_width() / 2, skull_y + skull.get_height() / 2))
            surface.blit(skull, (skull_x, skull_y))  # Display the skull image on the game over screen    Source: Canva AI
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
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
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        surface.fill(random_color())  # Change the background color to a random color each frame
        pygame.draw.rect(surface, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        update_high_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            eat_sound.play(loops=0)  # Play the eat sound when the snake eats the food



        # Increase the snake speed as the score increases, with a maximum speed limit to keep the game playable
        if (Length_of_snake - 1) > 30:
            snake_speed = 30  
        elif (Length_of_snake - 1) > 20:
            snake_speed = 25
        elif (Length_of_snake - 1) > 10:
            snake_speed = 20
        else: 
            snake_speed = 15
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()