from threading import currentThread
from tkinter import Button
from turtle import width
import pygame
import sys
import os
import ctypes
import random
from game import equation_generator
currentEquation, answer = equation_generator.main()
fakeanswer = equation_generator.fake_answer1(answer)
fakeanswer2 = equation_generator.fake_answer2(answer, fakeanswer)
print(currentEquation,   answer,   fakeanswer,   fakeanswer2)
user32 = ctypes.windll.user32
screenHeight = user32.GetSystemMetrics(0)
screenWidth = user32.GetSystemMetrics(1)
screen=pygame.display.set_mode((screenHeight,screenWidth))
print(screenHeight,screenWidth)
ANSWER_LIST = [answer, fakeanswer, fakeanswer2]
print(ANSWER_LIST)

light=pygame.image.load('assets\images\yellow_light.png') # radial gradient used for light pattern
bg = pygame.image.load('assets\images\hall.png')
skylight = pygame.image.load('assets\images\images.jpg')
skylight = pygame.transform.scale(skylight, (700, 250))
skylight_rect = skylight.get_rect()
door_color = ('#773600')
window_color = ('#9AE0F3')
heightScalar = screenWidth/720
widthScalar = screenHeight/1280
print(widthScalar)
door_width = 250*widthScalar  
door_height = 400*widthScalar
window_width = 200*widthScalar
window_height = 150*widthScalar
box_height = 200*widthScalar
box_width = 400*widthScalar
player = pygame.image.load(os.path.join('assets/torch.gif')).convert_alpha(); # load in player image, convert_alpha will keep transparent background

player = pygame.transform.scale(player, (150, 150)) # resize player
light=pygame.transform.scale(light, (800,800)) # resize gradient
bg = pygame.transform.scale(bg, (screenHeight,screenWidth))

night = True # boolean to set if it is night or day

while True:
    
    for e in pygame.event.get():
        if e.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0] in range(int(125*widthScalar),int((125*widthScalar)+(250*widthScalar))):
                    if pos[1] in range(int(300*widthScalar),int((300*widthScalar)+(400*widthScalar))):
                        print(1)
                        skylight = pygame.image.load('assets/images/cracked_window.jpg')
                        skylight = pygame.transform.scale(skylight, (700, 250))
                        skylight_rect = skylight.get_rect()
                elif pos[0] in range(int(525*widthScalar),int((525*widthScalar)+(250*widthScalar))):
                    if pos[1] in range(int(300*widthScalar),int((300*widthScalar)+(400*widthScalar))):
                        print(2)
                elif pos[0] in range(int(925*widthScalar),int((925*widthScalar)+(250*widthScalar))):
                    if pos[1] in range(int(300*widthScalar),int((300*widthScalar)+(400*widthScalar))):
                        print(3)
                
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit
                break
        if e.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
            break
        

    pygame.mouse.set_visible(True)
    pos = []
    pos = pygame.mouse.get_pos() # get mouse position
    #torch_pos = pos[0] - 67, pos[1]- 64 # torch_pos is the mouse position shifted over so the torch lines up with mouse correctly


    screen.fill(pygame.color.Color('Black')) # just a background
    screen.blit(bg,(0,0))
    #pygame.draw.rect(screen, door_color, pygame.Rect((125*widthScalar), (300*heightScalar), door_width, door_height))
    #pygame.draw.rect(screen, door_color, pygame.Rect((525*widthScalar), (300*heightScalar), door_width, door_height))
    #pygame.draw.rect(screen, door_color, pygame.Rect((925*widthScalar), (300*heightScalar), door_width, door_height))
    #pygame.draw.rect(screen, window_color, pygame.Rect((150*widthScalar), (325*heightScalar), window_width, window_height))
    #pygame.draw.rect(screen, window_color, pygame.Rect((550*widthScalar), (325*heightScalar), window_width, window_height))
    #pygame.draw.rect(screen, window_color, pygame.Rect((950*widthScalar), (325*heightScalar), window_width, window_height))

    #screen.blit(skylight, skylight_rect)
    
    #pygame.draw.circle(screen,'#FF00FF',((325*widthScalar),(550*widthScalar)),(25*widthScalar))
    #pygame.draw.circle(screen,'#FF00FF',((725*widthScalar),(550*widthScalar)),(25*widthScalar))
    #pygame.draw.circle(screen,'#FF00FF',((1125*widthScalar),(550*widthScalar)),(25*widthScalar))



    ############################################################################################
    # Joseph: Display Current Equation.
    #
    # Notes: For some reason, it sees 'render' with no attribute. That might be the only issue
    #        at the moment.
    ############################################################################################
    # # Added black variable (color of text?).
    pygame.init()

    # This is the RGB value for the colors.
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (153,19,9)
    # Create the display surface object of the specific dimention.

    # Added variable for the text style (text through GUI).
    font = pygame.font.Font("assets/fonts/BloodLust.ttf", 50) # ("font", text size)

    # Create a text surface object, on which text is drawn on it.
    # it was...text = pygame.font.render(currentEquation, True, black, white)
    text = font.render(currentEquation, True, black, white)


    # Create a rectangular object for the text surface object.
    textRect = text.get_rect()

    # Pass a string to myFond.render.
    display_equation = font.render(str(currentEquation), True, red)
    x = display_correct_answer = font.render(str(answer), True, red)
    y = display_fake_answer_one = font.render(str(fakeanswer), True, red)
    z = display_fake_answer_two = font.render(str(fakeanswer2), True, red)

    # Make screen blit funcitons to run things above.
    screen.blit(display_equation, (600, 150))
    screen.blit(x, (245, 425))
    screen.blit(y, (1075, 420))
    screen.blit(z, (675, 300))
   

    # pygame.display.update()

    # Commented out for now.
    # while True:

    #     # Pass a string to myFond.render.
    #     display_equation = font.render(str(currentEquation), True, white)

    #     # Make screen blit funcitons to run things above.
    #     #screen.blit(display_equation, (500, 10))
    #     display_surface.blit(text, textRect)

    # ############################################################################################



    if night: # if light effect needed
        filter = pygame.surface.Surface((screenHeight, screenWidth)) # create surface same size as window
        filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
        filter.blit(light,(pos[0]-367,pos[1]-364)) # blit light to the filter surface -400 is to center effect
        filter.blit(light,(screenHeight/2,screenWidth/2))
        screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MIN) # blit filter surface but with a blend

    #screen.blit(player,torch_pos) # blit the player over the effect
    pygame.display.flip()
    
    def lives_lost(answer):
        pygame.image('assets/images/cracked_window.jpg')
        if answer == False:
            skylight = pygame.image.load('cracked_window.jpg')
            skylight = pygame.transform.scale(skylight, (700, 250))
            
    class Player():

        def __init__(self):
            self.lives == 3
            if lives_lost(answer) == True:
                self.lives = -1


    

