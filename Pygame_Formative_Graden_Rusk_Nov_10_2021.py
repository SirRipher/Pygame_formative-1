#--------
#Pygame
#Graden_Rusk
#Nov_9_2021
#--------

#---Information---#
#1. In the getting started with pygame they used one main class for each blob that he made, he gave all of them the same attributes such as width
#height, and size and color. he didn't put the draw enviroment (function) in the class thogh because you may not want to have to use the class to
#get the information to use this function. Pygame also uses things like methods, these are basically just functions that are called within a class
#and all they may need is the self input. I think that this could probably be done without oop but the code would be very long and tedious
# the reason that I think it could be done is that you wuld have to use while loops to make the code make all of the dots, but what you would have to
#do is to have the code chech and see how many times it has called itself and each time the number changes it would use a different color.
# it would just be very tdious and you would probably have to save everything to lists too. I think.
#---classes---#

import pygame
import random
import time

Blue = (51, 236, 255)
Green = (196, 255, 51)
Purple = (253, 51, 255)
Blue_Dot = 3
Purple_Dot = 1
Width = 1000
Height = 600

print("The whole point of this game is to move the dot around on the screen, or just play hide and seek with the other dots.")
time.sleep(5)
game_display = pygame.display.set_mode((Width,Height))#note* anything with hashtags in front of them was code that i either tried and didn't need or it didn't work.
pygame.display.set_caption('Useless Moving Dot')
clock = pygame.time.Clock()

class Mainrun():
    
    def __init__(self, color):
        self.size = (12)
        self.color = color
        self.x = random.randrange(0, 1000, 25)
        self.y = random.randrange(0, 600, 25)
        
        #self.Rect = (30, 30, 60, 60)
        
        
#     def attribute(self):
#         self.x = (Width / 2)# I wanted it to start in the middle of the screen horizontaly.
#         self.y = (500)
        
#     def Dot(self):
#         self.x = 200
#         self.y = 575
#         Move(self)
        
    def move_1(self):
        for event in pygame.event.get():
                if event.type == 'QUIT':
                    pygame.quit()
                    sys.exit()
                elif event. type  == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x = self.x - 25
                    if event.key == pygame.K_RIGHT:# Thanks google
                        self.x = self.x + 25
                    if event.key == pygame.K_UP:
                        self.y = self.y - 25
                    if event.key == pygame.K_DOWN:
                        self.y = self.y + 25
                
                if self.x < 0: self.x = 0
                elif self.x > Width: self.x = Width
        
                if self.y < 0: self.y = 0
                elif self.y > Height: self.y = Height
        
def Move(Dots):
    game_display.fill(Green)

    for Dots_dict in Dots:
        for Dots_id in Dots_dict:#this is very confusing to look at.
            Dot = Dots_dict[Dots_id]
            pygame.draw.circle(game_display, Dot.color, [Dot.x, Dot.y], Dot.size)
            if Dot.color == Purple:
                Dot.move_1()

    pygame.display.update()
    #pygame.draw.circle(game_display, self.color, [self.x, self.y], self.size)
    #self.move_1()
    #pygame.display.update()
    
def main():
    person_Dot = dict(enumerate([Mainrun(Purple) for i in range(Purple_Dot)]))
    Blue_Dots = dict(enumerate([Mainrun(Blue) for i in range(Blue_Dot)]))
    #person = Mainrun(Green)
    #person.attribute()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        clock.tick(100) 
        Move([person_Dot,Blue_Dots])
        #Move(person)

#----Main Code Here----#
main()
