import pygame
import os
pygame.font.init()
pygame.mixer.init()
from classes import RED_SPACESHIP, YELLOW_SPACESHIP


# WIDTH, HEIGHT = 1500, 1000
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!") 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

FPS = 60
VEL = 5

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

YELLOW_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', YELLOW_SPACESHIP.image))
YELLOW_SPACESHIP_IMG = pygame.transform.scale(YELLOW_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
YELLOW_SPACESHIP_IMG = pygame.transform.rotate(YELLOW_SPACESHIP_IMG, 90)

RED_SPACESHIP_IMG = pygame.image.load(os.path.join('Assets', RED_SPACESHIP.image))
RED_SPACESHIP_IMG = pygame.transform.scale(RED_SPACESHIP_IMG, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_IMG = pygame.transform.rotate(RED_SPACESHIP_IMG, 270)

SPACE_BG = pygame.image.load(os.path.join('Assets', 'space.png'))
SPACE_BG = pygame.transform.scale(SPACE_BG, (WIDTH, HEIGHT))  

def draw_window(red, yellow):
    WIN.blit(SPACE_BG, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    WIN.blit(YELLOW_SPACESHIP_IMG, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMG, (red.x, red.y))

    pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]:
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + yellow.width < HEIGHT:
        yellow.y += VEL

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + 40 < WIDTH:
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + 55 < HEIGHT:
        red.y += VEL

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(750, HEIGHT//2 - SPACESHIP_WIDTH//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(150 - SPACESHIP_HEIGHT, HEIGHT//2 - SPACESHIP_WIDTH//2, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        if red.x < BORDER.x:
            RED_SPACESHIP.vulnerable == True
        else:
            RED_SPACESHIP.vulnerable == False

        if yellow.x + yellow.width > BORDER.x + BORDER.width:
            YELLOW_SPACESHIP.vulnerable == True
        else:
            YELLOW_SPACESHIP.vulnerable == False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == RED_HIT:
                BULLET_HIT_SOUND.play()
                
            if event.type == YELLOW_HIT:
                BULLET_HIT_SOUND.play()

        if yellow.colliderect(red):
        # if yellow.colliderect(red) and RED_SPACESHIP.vulnerable:
            # pygame.event.post(pygame.event.Event(YELLOW_HIT))
            print('red hit!')
        # if yellow.colliderect(red) and YELLOW_SPACESHIP.vulnerable:
        if yellow.colliderect(red):
            print('yel hit!')


        winner_text = ''
        # if red_health <= 0:
        #     winner_text = 'Yellow Wins!'
        # if yellow_health <= 0:
        #     winner_text = 'Red Wins!'
        if winner_text != '':
            draw_winner(winner_text)
            break
                    
        keys_pressed = pygame.key.get_pressed()

        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        draw_window(red, yellow)

        if keys_pressed[pygame.K_x]:
            pygame.quit()
        if keys_pressed[pygame.K_t]:
            main()

    main()

if __name__ == "__main__":
    main()