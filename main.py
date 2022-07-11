from threading import currentThread
from tkinter import Button
from turtle import width
import pygame
import sys
import os
import ctypes
import random
from game import equation_generator
pygame.init()
# Adds the music library from pygame.
from pygame import mixer



class Game():
    def __init__(self):

        # Calls the music file and plays during the game.
        mixer.init()
        mixer.music.load('assets/music/Scary_Music_1.mp3')
        mixer.music.play()
        
        #print(self.currentEquation,   self.answer,   self.fakeanswer,   self.fakeanswer2)
        self.user32 = ctypes.windll.user32
        self.screenHeight = self.user32.GetSystemMetrics(0)
        self.screenWidth = self.user32.GetSystemMetrics(1)
        self.screen=pygame.display.set_mode((self.screenHeight,self.screenWidth))
        
        # ANSWER_LIST = [self.answer, self.fakeanswer, self.fakeanswer2]


        self.light=pygame.image.load('assets\images\white.png') # radial gradient used for light pattern
        self.candlelight = pygame.image.load('assets\images\yellow_light.png')
        self.bg = pygame.image.load('assets\images\hall.png')
        #self.flashlight = pygame.image.load('assets\images\flashlight.png') #flashlight sprite at bottom of screen
     
    
        self.heightScalar = self.screenWidth/720
        self.widthScalar = self.screenHeight/1280
       
        self.player = pygame.image.load(os.path.join('assets/torch.gif')).convert_alpha(); # load in player image, convert_alpha will keep transparent background

        self.player = pygame.transform.scale(self.player, (150, 150)) # resize player
        self.light=pygame.transform.scale(self.light, (900,900)) # resize gradient
        self.candlelight=pygame.transform.scale(self.candlelight, (600,600))
        self.bg = pygame.transform.scale(self.bg, (self.screenHeight,self.screenWidth))

        self.night = True # boolean to set if it is night or day

        
        pygame.init()

        # This is the RGB value for the colors.
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (153,19,9)
        # Create the display surface object of the specific dimention.
        # Added variable for the text style (text through GUI).
        self.font = pygame.font.Font("assets/fonts/BloodLust.ttf", 50) # ("font", text size)
        self.score = 0


    def game_loop(self):

        self.currentEquation, self.answer = equation_generator.main()
        self.fakeanswer = equation_generator.fake_answer1(self.answer)
        self.fakeanswer2 = equation_generator.fake_answer2(self.answer, self.fakeanswer)

         # Create a text surface object, on which text is drawn on it.
        # it was...text = pygame.font.render(currentEquation, True, black, white)
        self.text = self.font.render(self.currentEquation, True, self.black, self.white)


        # Create a rectangular object for the text surface object.
        self.textRect = self.text.get_rect()

        # Pass a string to myFond.render.

        correct_position = random.randint(1,3)
        print(correct_position)

        self.display_equation = self.font.render(str(self.currentEquation), True, self.red)
        if correct_position == 1:
            self.x = self.font.render(str(self.answer), True, self.red)
            self.y = self.font.render(str(self.fakeanswer), True, self.red)
            self.z = self.font.render(str(self.fakeanswer2), True, self.red)
        elif correct_position == 3:
            self.x = self.font.render(str(self.fakeanswer), True, self.red)
            self.y = self.font.render(str(self.answer), True, self.red)
            self.z = self.font.render(str(self.fakeanswer2), True, self.red)
        elif correct_position == 2:
            self.x = self.font.render(str(self.fakeanswer), True, self.red)
            self.y = self.font.render(str(self.fakeanswer2), True, self.red)
            self.z = self.font.render(str(self.answer), True, self.red)

        self.scored = self.font.render("Score: " + str(self.score), True, self.red)
        loop = True
        selected = 0
        guesses = 2
        chosen = set()

        # Created variables for the correct and wrong answers when selecting a door.
        correct_sound = pygame.mixer.Sound("assets/music/Correct_Answer.mp3")
        wrong_sound = pygame.mixer.Sound("assets/music/Wrong_Answer.mp3")

        while loop == True:

            for e in pygame.event.get():
                if e.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
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
                    else:
                        selected = 0
                    if selected == correct_position:
                        if len(chosen) == 0:
                            self.score += 100
                            print(self.score)
                            pygame.mixer.Sound.play(correct_sound)


                        elif len(chosen) == 1:
                            self.score += 50
                            print(self.score)

                        
                        loop = False
                        self.game_loop()

                    elif selected != 0:
                        if selected != correct_position:
                            pygame.mixer.Sound.play(wrong_sound)

                            if selected not in chosen:
                                chosen.add(selected)
                                guesses -= 1
                            else:
                                chosen.add(selected)
                                pass
                        if guesses == 0:
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

            self.screen.blit(self.display_equation, (900, 200))
            self.screen.blit(self.x, (245 * self.widthScalar, 400 * self.heightScalar))
            self.screen.blit(self.y, (1000 * self.widthScalar, 400 * self.heightScalar))
            self.screen.blit(self.z, (625 * self.widthScalar, 300 * self.heightScalar))
            self.screen.blit(self.scored, (730 * self.widthScalar, 200 * self.heightScalar))
        

            if self.night: # if light effect needed
                filter = pygame.surface.Surface((self.screenHeight, self.screenWidth)) # create surface same size as window
                filter.fill(pygame.color.Color('Black')) # Black will give dark unlit areas, Grey will give you a fog
                filter.blit(self.light,(380 * self.widthScalar, -100 * self.heightScalar))
                filter.blit(self.candlelight,(600 * self.widthScalar, 160* self.heightScalar))
                filter.blit(self.candlelight,(640 * self.widthScalar, 160* self.heightScalar))
                filter.blit(self.light,(self.pos[0]-450,self.pos[1]-450)) # blit light to the filter surface -400 is to center effect
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


    

