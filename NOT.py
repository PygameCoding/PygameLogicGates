# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([600, 200])
pygame.display.set_caption('NOT gate demo')

# initialize the inputs
input1 = False
offtexture = pygame.image.load("Logic Gates/0BOX.png").convert_alpha()
ontexture = pygame.image.load("Logic Gates/1BOX.png").convert_alpha()
notgate = pygame.image.load("Logic Gates/Notgate.png").convert_alpha()

#button class
class Gate():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

Input = Gate(100, 400, offtexture)
coll = pygame.draw.rect(screen, (0, 0, 0), (50, 50, 100, 100))




# Run until the user asks to quit
running = True
while running:

    if input1 == True:
        Output = Gate(450, 50, offtexture)
    else:
        Output = Gate(450, 50, ontexture)
    if input1 == True:
        Input = Gate(50, 50, ontexture)
    else:
        Input = Gate(50, 50, offtexture)
    
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    print(mouse)
    print(click[0])
    if click[0] == 1 and mouse[0] > 0 and mouse[0] < 600 and mouse[1] > 50 and mouse[1] < 150:

        if input1 == True:
            input1 = False
        else:
            input1 = True
        time.sleep(0.2)
    

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    screen.blit(notgate, (150, 50))
    Output.draw()
    Input.draw()


    # Flip the display
    pygame.display.update()

# Done! Time to quit.
pygame.quit()