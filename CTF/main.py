import pygame
import os
pygame.font.init()
pygame.mixer.init()
from classes import red_spaceship, yellow_spaceship


width, height = 1440, 790
# width, height = 900, 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("First Game!") 

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

fps = 60
vel = 5

spaceship_width, spaceship_height = 55, 40

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2
ky_flag_capt = pygame.USEREVENT + 3
nj_flag_capt = pygame.USEREVENT + 4

border = pygame.Rect(width//2 - 5, 0, 10, height)

bullet_hit_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
bullet_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))

health_font = pygame.font.SysFont('comicsans', 40)
winner_font = pygame.font.SysFont('comicsans', 100)

yellow_spaceship_img = pygame.image.load(os.path.join('Assets', yellow_spaceship.image))
yellow_spaceship_img = pygame.transform.scale(yellow_spaceship_img, (spaceship_width, spaceship_height))
yellow_spaceship_img = pygame.transform.rotate(yellow_spaceship_img, 90)

red_spaceship_img = pygame.image.load(os.path.join('Assets', red_spaceship.image))
red_spaceship_img = pygame.transform.scale(red_spaceship_img, (spaceship_width, spaceship_height))
red_spaceship_img = pygame.transform.rotate(red_spaceship_img, 270)

ky_flag_img = pygame.image.load(os.path.join('Assets', 'ky_flag.png'))
ky_flag_img = pygame.transform.scale(ky_flag_img, (spaceship_width, spaceship_height))
nj_flag_img = pygame.image.load(os.path.join('Assets', 'nj_flag.png'))
nj_flag_img = pygame.transform.scale(nj_flag_img, (spaceship_width, spaceship_height))

space_bg = pygame.image.load(os.path.join('Assets', 'space.png'))
space_bg = pygame.transform.scale(space_bg, (width, height))  

def draw_window(red, yellow, ky_flag_bool, nj_flag_bool):
    win.blit(space_bg, (0,0))
    pygame.draw.rect(win, black, border)

    win.blit(yellow_spaceship_img, (yellow.x, yellow.y))
    win.blit(red_spaceship_img, (red.x, red.y))

    # win.blit(ky_flag_img, (red.x + spaceship_height, red.y + 8))
    win.blit(ky_flag_img, (1290, 376))

    if nj_flag_bool == True:
        win.blit(nj_flag_img, (red.x + spaceship_height, red.y + 8))
    else:
        win.blit(nj_flag_img, (95, 376))

    pygame.display.update()

def yellow_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x > 0:
        yellow.x -= vel
    if keys_pressed[pygame.K_d]:
        yellow.x += vel
    if keys_pressed[pygame.K_w] and yellow.y > 0:
        yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + yellow.width < height:
        yellow.y += vel

def red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT]:
        red.x -= vel
    if keys_pressed[pygame.K_RIGHT] and red.x + 40 < width:
        red.x += vel
    if keys_pressed[pygame.K_UP] and red.y > 0:
        red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + 55 < height:
        red.y += vel

def red_ship_reset(red):
    red.x = width - 150 - spaceship_height
    red.y = height//2 - spaceship_width//2

def yellow_ship_reset(yellow):
    yellow.x = 150
    yellow.y = height//2 - spaceship_width//2

def draw_winner(text):
    draw_text = winNER_FONT.render(text, 1, white)
    win.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(width - 150 - spaceship_height, height//2 - spaceship_width//2, spaceship_width, spaceship_height)
    yellow = pygame.Rect(150, height//2 - spaceship_width//2, spaceship_width, spaceship_height)

    ky_flag_rect = pygame.Rect(1290, 376, spaceship_width, spaceship_height)
    nj_flag_rect = pygame.Rect(95, 376, spaceship_width, spaceship_height)

    ky_flag_bool = False
    nj_flag_bool = False


    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)

        if red.x < border.x:
            red_spaceship.vulnerable = True
        else:
            red_spaceship.vulnerable = False

        if yellow.x + yellow.width > border.x + border.width:
            yellow_spaceship.vulnerable = True
        else:
            yellow_spaceship.vulnerable = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == red_hit:
                red_ship_reset(red)
                
            if event.type == yellow_hit:
                yellow_ship_reset(yellow)

            if event.type == ky_flag_capt:
                ky_flag_bool = True

            if event.type == nj_flag_capt:
                nj_flag_bool = True


        if yellow.colliderect(red) and red_spaceship.vulnerable:
            pygame.event.post(pygame.event.Event(red_hit))

        if yellow.colliderect(red) and yellow_spaceship.vulnerable:
            pygame.event.post(pygame.event.Event(yellow_hit))

        if yellow.colliderect(ky_flag_rect):
            pygame.event.post(pygame.event.Event(ky_flag_capt))

        if red.colliderect(nj_flag_rect):
            pygame.event.post(pygame.event.Event(nj_flag_capt))


        winner_text = ''
        # if red_health <= 0:
        #     winner_text = 'yellow wins!'
        # if yellow_health <= 0:
        #     winner_text = 'red wins!'
        if winner_text != '':
            draw_winner(winner_text)
            break
                    
        keys_pressed = pygame.key.get_pressed()

        yellow_movement(keys_pressed, yellow)
        red_movement(keys_pressed, red)

        draw_window(red, yellow, ky_flag_bool, nj_flag_bool)

        if keys_pressed[pygame.K_x]:
            pygame.quit()
        if keys_pressed[pygame.K_t]:
            main()

    main()

if __name__ == "__main__":
    main()