import pygame
import sys
import os
import ctypes


user32 = ctypes.windll.user32
screenHeight = user32.GetSystemMetrics(0)
screenWidth = user32.GetSystemMetrics(1)
screen=pygame.display.set_mode((screenHeight,screenWidth))


light=pygame.image.load('assets\images\yellow_light.png') # radial gradient used for light pattern
bg = pygame.image.load('assets\images\yY7suH.png')
door_color = ('#773600')
window_color = ('#9AE0F3')
door_width = 250
door_height = 400
window_width = 200
window_height = 150
box_height = 200
box_width = 400
player = pygame.image.load(os.path.join('assets/torch.gif')).convert_alpha(); # load in player image, convert_alpha will keep transparent background

player = pygame.transform.scale(player, (150, 150)) # resize player
light=pygame.transform.scale(light, (800,800)) # resize gradient
bg = pygame.transform.scale(bg, (screenHeight,screenWidth))

night = True # boolean to set if it is night or day

while True:
    
    for e in pygame.event.get():
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit
                break
        if e.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
            break

        if e.type == pygame.MOUSEBUTTONDOWN:
            night = not night # toggle night between true and false

    pygame.mouse.set_visible(False)
    pos = []
    pos = pygame.mouse.get_pos() # get mouse position
    torch_pos = pos[0] - 67, pos[1]- 64 # torch_pos is the mouse position shifted over so the torch lines up with mouse correctly


    screen.fill(pygame.color.Color('Black')) # just a background
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen, door_color, pygame.Rect(125, 300, door_width, door_height))
    pygame.draw.rect(screen, door_color, pygame.Rect(525, 300, door_width, door_height))
    pygame.draw.rect(screen, door_color, pygame.Rect(925, 300, door_width, door_height))
    pygame.draw.rect(screen, window_color, pygame.Rect(150, 325, window_width, window_height))
    pygame.draw.rect(screen, window_color, pygame.Rect(550, 325, window_width, window_height))
    pygame.draw.rect(screen, window_color, pygame.Rect(950, 325, window_width, window_height))
    pygame.draw.rect(screen, '#FFFFFF', pygame.Rect(0, 0, box_width, box_height))
    pygame.draw.circle(screen,'#FF00FF',(325,550),25)
    pygame.draw.circle(screen,'#FF00FF',(725,550),25)
    pygame.draw.circle(screen,'#FF00FF',(1125,550),25)



    if night: # if light effect needed
        filter = pygame.surface.Surface((screenHeight, screenWidth)) # create surface same size as window
        filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
        filter.blit(light,(pos[0]-367,pos[1]-364)) # blit light to the filter surface -400 is to center effect
        screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MIN) # blit filter surface but with a blend

    screen.blit(player,torch_pos) # blit the player over the effect
    pygame.display.flip()
