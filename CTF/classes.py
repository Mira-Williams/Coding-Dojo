class Spaceship:
    def __init__(self, color, speed, vulnerable, width, height, image):
        self.color = color
        self.speed = speed
        self.vulnerable = vulnerable
        self.width = width
        self.height = height
        self.image = image
        

RED_SPACESHIP = Spaceship('red', 5, False, 55, 40, 'spaceship_red.png')
YELLOW_SPACESHIP = Spaceship('yellow', 5, False, 55, 40, 'spaceship_yellow.png')

test = 'test 1'
