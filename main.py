from threading import currentThread
from tkinter import Button
from turtle import width
import pygame
import sys
import os
import ctypes
import random
from game import equation_generator

class Game():
    def __init__(self):

        
        #print(self.currentEquation,   self.answer,   self.fakeanswer,   self.fakeanswer2)
        self.user32 = ctypes.windll.user32
        self.screenHeight = self.user32.GetSystemMetrics(0)
        self.screenWidth = self.user32.GetSystemMetrics(1)
        self.screen=pygame.display.set_mode((self.screenHeight,self.screenWidth))
        
        # ANSWER_LIST = [self.answer, self.fakeanswer, self.fakeanswer2]


        self.light=pygame.image.load('assets\images\yellow_light.png') # radial gradient used for light pattern
        self.bg = pygame.image.load('assets\images\hall.png')
        
     
        self.heightScalar = self.screenWidth/720
        self.widthScalar = self.screenHeight/1280
       
        self.player = pygame.image.load(os.path.join('assets/torch.gif')).convert_alpha(); # load in player image, convert_alpha will keep transparent background

        self.player = pygame.transform.scale(self.player, (150, 150)) # resize player
        self.light=pygame.transform.scale(self.light, (800,800)) # resize gradient
        self.bg = pygame.transform.scale(self.bg, (self.screenHeight,self.screenWidth))

        self.night = False # boolean to set if it is night or day

        
        pygame.init()

        # This is the RGB value for the colors.
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (153,19,9)
        # Create the display surface object of the specific dimention.
        # Added variable for the text style (text through GUI).
        self.font = pygame.font.Font("assets/fonts/BloodLust.ttf", 50) # ("font", text size)


    def game_loop(self):
        self.currentEquation, self.answer = equation_generator.main()
        self.fakeanswer = equation_generator.fake_answer1(self.answer)
        self.fakeanswer2 = equation_generator.fake_answer2(self.answer)

         # Create a text surface object, on which text is drawn on it.
        # it was...text = pygame.font.render(currentEquation, True, black, white)
        self.text = self.font.render(self.currentEquation, True, self.black, self.white)


        # Create a rectangular object for the text surface object.
        self.textRect = self.text.get_rect()

        # Pass a string to myFond.render.
        self.display_equation = self.font.render(str(self.currentEquation), True, self.red)
        self.x = self.font.render(str(self.answer), True, self.red)
        self.y = self.font.render(str(self.fakeanswer), True, self.red)
        self.z = self.font.render(str(self.fakeanswer2), True, self.red)

        loop = True
        selected = 0
        correct_position = 1
        while loop == True:
            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if pos[0] in range(int(200*self.widthScalar),int((315*self.widthScalar))):
                        if pos[1] in range(int(200*self.widthScalar),int((525*self.widthScalar))):
                            print(1)
                            selected = 1
                    elif pos[0] in range(int(580*self.widthScalar),int((715*self.widthScalar))):
                        if pos[1] in range(int(160*self.widthScalar),int((370*self.widthScalar))):
                            print(2)
                            selected = 2
                    elif pos[0] in range(int(970*self.widthScalar),int((1100*self.widthScalar))):
                        if pos[1] in range(int(190*self.widthScalar),int((530*self.widthScalar))):
                            print(3)
                            selected = 3
                    if selected == correct_position:
                        loop = False
                        self.game_loop()
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
                self.pos = []
                self.pos = pygame.mouse.get_pos() # get mouse position

        # Make screen blit funcitons to run things above.
            self.screen.fill(pygame.color.Color('Black')) # just a background
            self.screen.blit(self.bg,(0,0))

            self.screen.blit(self.display_equation, (600, 150))
            self.screen.blit(self.x, (245 * self.widthScalar, 400 * self.heightScalar))
            self.screen.blit(self.y, (1075 * self.widthScalar, 420 * self.heightScalar))
            self.screen.blit(self.z, (675 * self.widthScalar, 300 * self.heightScalar))
        

            if self.night: # if light effect needed
                filter = pygame.surface.Surface((self.screenHeight, self.screenWidth)) # create surface same size as window
                filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
                filter.blit(self.light,(pos[0]-367,pos[1]-364)) # blit light to the filter surface -400 is to center effect
                filter.blit(self.light,(self.screenHeight/2,self.screenWidth/2))
                self.screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_MIN) # blit filter surface but with a blend

            pygame.display.flip()


    #screen.blit(player,torch_pos) # blit the player over the effect
    #pygame.display.flip()
    
    # def lives_lost(answer):
    #     if answer == False:
            
class Player():
    pass

def main():
    game = Game()
    game.game_loop()

if __name__ == "__main__":
    main()


    

